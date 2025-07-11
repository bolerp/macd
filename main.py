import asyncio
import logging
import sys
import csv
from datetime import datetime, timezone
from pathlib import Path

import requests  # для получения marketcap

from dotenv import load_dotenv

# ----------------------------- Логирование ---------------------------------
LOG_LEVEL = logging.DEBUG if "--debug" in sys.argv else logging.INFO
# ----------------------- Логирование в консоль + файл ---------------------

# Создаём директорию logs, если нет
LOG_DIR = Path("logs")
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Формируем имя файла с таймстампом
_ts = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
RUN_LOG_PATH = LOG_DIR / f"scan_{_ts}.log"

logging.basicConfig(
    level=LOG_LEVEL,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.StreamHandler(sys.stdout),  # вывод в консоль
        logging.FileHandler(RUN_LOG_PATH, encoding="utf-8"),  # полный лог в файл
    ],
    force=True,
)
logger = logging.getLogger(__name__)

# --- Импорты, которым требуется настроенный логгер -----------------------
from alerter import escape_markdown_v2, send_telegram_alert, send_telegram_photo
from data_provider import get_target_pairs, check_liquidity
from scanner import analyze_pair
from chart_utils import generate_chart

# ──────────── Helper: получить market-cap из DexScreener ────────────
_MC_CACHE: dict[str, float] = {}


def get_marketcap_usd(mint: str) -> float | None:
    """Возвращает FDV/marketCap USD для токена по его mint-адресу.

    Запрашиваем API DexScreener, кешируем ответ чтобы не обращаться к
    сервису много раз за один прогон.
    """
    if mint in _MC_CACHE:
        return _MC_CACHE[mint]

    url = f"https://api.dexscreener.com/latest/dex/tokens/{mint}"
    try:
        resp = requests.get(url, timeout=10)
        data = resp.json()
        if data.get("pairs"):
            pair = data["pairs"][0]
            mc_val = pair.get("fdv") or pair.get("marketCap")
            if mc_val:
                _MC_CACHE[mint] = float(mc_val)
                return float(mc_val)
    except Exception as exc:  # noqa: BLE001
        logger.debug("Не удалось получить marketcap для %s: %s", mint, exc)

    return None


# ----------------------- Сообщение об одном сигнале ------------------------

def build_message(symbol: str, name: str, mint: str, info: dict, mcap: float | None) -> str:
    """Формирует красивое и безопасное MarkdownV2-сообщение о сигнале."""

    # Экранируем только те части, что приходят от пользователя
    safe_symbol = escape_markdown_v2(symbol)
    safe_name = escape_markdown_v2(name)

    # Форматируем числа
    price_str = f"{info['close']:.6f}".rstrip("0").rstrip(".")
    volume_k = int(info['volumeUSD']) // 1_000
    mc_line = f"🏦 *МаркКап:* `${mcap/1_000_000:.2f}M`" if mcap else "🏦 *МаркКап:* `n/a`"
    arrow = "📈" if info['macd_curr'] > info['macd_prev'] else "📉"

    # Собираем сообщение
    lines = [
        # ВАЖНО: Экранируем тире (минус) прямо здесь
        f"🚨 *MACD\\-сигнал* {arrow}",
        "",
        f"🏷️ *Токен:* `{safe_symbol}` \\({safe_name}\\)",
        f"🔑 *Контракт:* `{mint}`",
        f"💵 *Цена:* `${price_str}`",
        mc_line,
        f"📊 *MACD:* `{info['macd_prev']:.6f}` → `{info['macd_curr']:.6f}`",
        f"💸 *Объём:* `${volume_k}k`",
        "",
        f"🔗 [DexScreener](https://dexscreener.com/solana/{mint}) "
        f"\\| [Birdeye](https://birdeye.so/token/{mint}?chain=solana)"
    ]
    return "\n".join(lines)


# ------------------------------- Основной цикл -----------------------------

async def scan_and_alert(limit: int = 50):
    logger.info("Запуск сканирования… (limit=%s)", limit)
    charts_enabled = "--no-chart" not in sys.argv  # можно отключить графики

    # CSV-файл для токенов, прошедших TVL, но без MACD сигнала
    fail_csv_path = LOG_DIR / f"tvl_ok_macd_fail_{_ts}.csv"
    csv_file = fail_csv_path.open("w", newline="", encoding="utf-8")
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(["symbol", "name", "mint", "macd_prev", "macd_curr"])

    sent_today = set()  # простой анти-дупликатор

    pairs = get_target_pairs(limit=limit)

    # Дедупликация: один токен может встречаться в нескольких маркетах → берём первый
    unique_pairs = {}
    for p in pairs:
        mint = p.get("mintAddress")
        if mint and mint not in unique_pairs:
            unique_pairs[mint] = p

    pairs = list(unique_pairs.values())
    logger.info("Получено %d пар (уникальных токенов: %d)", len(pairs), len(pairs))

    for token in pairs:
        mint = token["mintAddress"]
        symbol = token.get("symbol", "?")
        name = token.get("name", "")

        if mint in sent_today:
            continue

        logger.info("Проверяем %s (%s) | mint: %s", symbol, name, mint)

        # Проверка ликвидности
        if not check_liquidity(mint):
            logger.info("%s – недостаточно TVL | mint: %s", symbol, mint)
            continue

        logger.info("%s – TVL норм, анализируем MACD... | mint: %s", symbol, mint)
        info = analyze_pair(mint)
        if not info:
            logger.info("%s – нет MACD-пересечения | mint: %s", symbol, mint)
            # Логируем в CSV файл подробности
            try:
                # пишем пустые значения macd, т.к. анализ вернул None
                csv_writer.writerow([symbol, name, mint, "", ""])
            except Exception:
                pass
            continue

        mcap = get_marketcap_usd(mint)
        message = build_message(symbol, name, mint, info, mcap)

        if charts_enabled:
            try:
                chart = generate_chart(mint, symbol)
                if chart:
                    await send_telegram_photo(chart, message)
                else:
                    await send_telegram_alert(message)
            except Exception as e:             # если рисование/отправка упало
                logger.exception("Не удалось сгенерировать или отправить график для %s: %s", symbol, e)
                await send_telegram_alert(message)
        else:
            await send_telegram_alert(message)

        sent_today.add(mint)
        logger.info("Сигнал отправлен: %s", symbol)

    logger.info("Сканирование завершено. Сигналов: %d", len(sent_today))
    # Закрываем CSV
    csv_file.close()


# ------------------------------ Точка входа --------------------------------

async def main():
    """CLI entry point.

    --test  : отправить тестовое сообщение и выйти
    --scan  : выполнить сканирование (по умолчанию)
    """

    if "--test" in sys.argv:
        raw = "Бот запущен и готов к работе! Это *тестовое* сообщение с форматированием."
        await send_telegram_alert(escape_markdown_v2(raw))
        logger.info("Тестовое сообщение отправлено.")
        return

    # По умолчанию сканируем
    limit = 500
    if "--limit" in sys.argv:
        try:
            idx = sys.argv.index("--limit")
            limit = int(sys.argv[idx + 1])
        except Exception:  # noqa: BLE001
            logger.warning("Неверное значение для --limit, используется 50")

    await scan_and_alert(limit=limit)


if __name__ == "__main__":
    # Загружаем переменные окружения из .env в текущей директории
    load_dotenv(override=True)

    asyncio.run(main()) 
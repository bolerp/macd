"""
Тестовая генерация графика (цена + MACD) и отправка в Telegram.

Использование:
    python test_chart_macd.py <mint_address> <symbol> [--days 90]

Пример:
    python test_chart_macd.py 9BB6...pump VINE --days 120
"""
import io
import sys
import asyncio
from datetime import datetime
from pathlib import Path

import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
from dotenv import load_dotenv

from ta.trend import MACD

from matplotlib import dates as md

# импортируем вашу логику
from data_provider import get_ohlcv_data
from alerter import escape_markdown_v2, send_telegram_alert  # используем уже готовую функцию

# ---------------------------------------------------------------------------

def calc_macd(df: pd.DataFrame) -> pd.DataFrame:
    macd = MACD(df["Close"], window_slow=26, window_fast=12, window_sign=9)
    df["MACD"] = macd.macd()
    df["MACD_Signal"] = macd.macd_signal()
    return df


def make_chart(df: pd.DataFrame, symbol: str) -> bytes:
    """
    Рисует свечной график + MACD за последние ~50 дней, возвращает PNG в виде bytes.
    """
    # берём последние 50 дней — хороший баланс контекста и фокуса
    df_recent = df.tail(50).copy()
    df_plot = df_recent.set_index("Date")

    # ──────────────────────────────────────────────────────────────
    # 1.  Подготовим стили с белым текстом
    dark = mpf.make_mpf_style(
        base_mpf_style = "binance",
        marketcolors = mpf.make_marketcolors(
            up    = "#26a69a",   
            down  = "#ef5350",
            wick  = {"up":"#26a69a","down":"#ef5350"},
            edge  = {"up":"#26a69a","down":"#ef5350"},
            volume={"up":"#26a69a","down":"#ef5350"},
        ),
        facecolor = "#141518",      
        figcolor  = "#141518",      
        gridstyle = "--",                 # ← включаем пунктирную сетку
        rc = {
            "axes.grid"     : True,       # ← сетка активна
            "grid.color"    : "#444444",
            "grid.alpha"    : 0.25,
            "font.size"     : 12,
            "text.color"    : "white",
            "axes.labelcolor": "white",
            "xtick.color"   : "white",
            "ytick.color"   : "white",
            "axes.edgecolor": "white",
        }
    )

    # ──────────────────────────────────────────────────────────────
    # 2.  addplot: MACD, сигнал, гистограмма
    macd_hist = df_plot["MACD"] - df_plot["MACD_Signal"]
    macd_colors = ["#26a69a" if v >= 0 else "#ef5350" for v in macd_hist]

    ap_macd_hist = mpf.make_addplot(macd_hist, panel=1, type="bar",
                                    color=macd_colors, alpha=0.5, ylabel="MACD")
    ap_macd   = mpf.make_addplot(df_plot["MACD"],        panel=1, color="#2196f3", width=1.2)
    ap_signal = mpf.make_addplot(df_plot["MACD_Signal"], panel=1, color="#ffa726", width=1.2)
    ap_zero   = mpf.make_addplot([0]*len(df_plot), panel=1,
                                 color="#888888", width=1, linestyle="--")

    # ──────────────────────────────────────────────────────────────
    # 3.  Сам график
    fig, axes = mpf.plot(
        df_plot,
        type         ="candle",
        style        =dark,
        addplot      =[ap_macd_hist, ap_macd, ap_signal, ap_zero],
        panel_ratios =(3,1.5),
        volume       =False,
        ylabel       ="Price ($)",
        tight_layout =True,
        returnfig    =True,
        figsize      =(14,8),
        title        ="",   # ← пусто, заголовок зададим вручную
    )

    # ──────────────────────────────────────────────────────────────
    # 4. Дополнительно принудительно делаем весь текст белым
    for ax in fig.get_axes():
        ax.tick_params(colors='white', labelsize=11)
        ax.yaxis.label.set_color('white')
        ax.xaxis.label.set_color('white')
        ax.title.set_color('white')
        
    # заголовок тоже белым
    fig.suptitle(f"{symbol} — Last 50 Days (MACD Signal)", color='white', fontsize=14)

    # -------- 5. косметика ------
    ax_price, ax_macd = axes[0], axes[2]          # price-панель и MACD-панель

    # Один(!) заголовок, чуть ниже верхней рамки
    fig.suptitle(f"{symbol} — Last 50 Days (MACD Signal)",
                 color="white", fontsize=14, y=0.98)

    # «Умные» даты: библиотека сама подбирает шаг тиков
    locator   = md.AutoDateLocator(minticks=5, maxticks=8)   # from matplotlib.dates as md
    formatter = md.DateFormatter("%d %b")   # 11 Jul, 15 Jun и т.д.

    # ──────────────────────────────────────────────────────────────
    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=120, bbox_inches="tight", facecolor='#141518')
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()

# ---------------------------------------------------------------------------

async def send_photo_alert(image_bytes: bytes, caption: str):
    """
    Отправляем фото тем же способом, что и текст.
    """
    import os, telegram
    from telegram.constants import ParseMode

    token = os.getenv("TELEGRAM_BOT_TOKEN")
    chat_ids = os.getenv("TELEGRAM_CHAT_IDS", "").split(",")

    bot = telegram.Bot(token=token)

    for cid in [c.strip() for c in chat_ids if c.strip()]:
        await bot.send_photo(
            chat_id=cid,
            photo=image_bytes,
            caption=caption,
            parse_mode=ParseMode.MARKDOWN_V2,
        )

# ---------------------------------------------------------------------------

async def main():
    load_dotenv()

    if len(sys.argv) < 3:
        print("python test_chart_macd.py <mint> <symbol> [--days 90]")
        return

    mint   = sys.argv[1]
    symbol = sys.argv[2]
    days   = 90
    if "--days" in sys.argv:
        idx = sys.argv.index("--days")
        days = int(sys.argv[idx + 1])

    print("🔄 Загружаем данные…")
    df = get_ohlcv_data(mint, days=days)
    if df.empty:
        print("Нет данных")
        return

    df = calc_macd(df)

    print("🎨 Рисуем график…")
    img = make_chart(df, symbol)

    # Формируем краткую подпись
    last = df.iloc[-1]
    prev = df.iloc[-2]
    arrow = "📈" if last["MACD"] > prev["MACD"] else "📉"
    caption = "\n".join([
        f"*{escape_markdown_v2(symbol)}*  {arrow}",
        f"Цена: `{last['Close']:.6g}`  USD",
        f"MACD: `{prev['MACD']:.6g}` → `{last['MACD']:.6g}`",
        f"[DexScreener](https://dexscreener.com/solana/{mint})"
    ])

    print("📤 Отправляем в Telegram…")
    await send_photo_alert(img, caption)
    print("✅ Готово")

# ---------------------------------------------------------------------------

if __name__ == "__main__":
    asyncio.run(main()) 
import os
import logging
import telegram
from telegram.constants import ParseMode

logger = logging.getLogger(__name__)

# --- отправка сообщений -----------------------------------------------------
async def send_telegram_alert(message: str):
    """
    Отправляет сообщение в несколько чатов.
    В .env задайте:
        TELEGRAM_BOT_TOKEN=xxxxx
        TELEGRAM_CHAT_IDS=111111111,222222222
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN не задан в .env")
        return

    raw_ids = os.getenv("TELEGRAM_CHAT_IDS", "")
    chat_ids = [cid.strip() for cid in raw_ids.split(",") if cid.strip()]
    if not chat_ids:
        logger.error("TELEGRAM_CHAT_IDS не задан или пуст")
        return

    bot = telegram.Bot(token=token)

    for cid in chat_ids:
        try:
            await bot.send_message(
                chat_id=cid,
                text=message,
                parse_mode=ParseMode.MARKDOWN_V2
            )
            logger.info(f"Отправлено в chat_id={cid}")
        except telegram.error.BadRequest as e:
            logger.error(f"BadRequest для {cid}: {e}")
        except telegram.error.TelegramError as e:
            logger.error(f"TelegramError для {cid}: {e}")

async def send_telegram_photo(image_bytes: bytes, caption: str):
    """
    Отправляет картинку + подпись (MarkdownV2) во ВСЕ chat-id из TELEGRAM_CHAT_IDS.
    """
    token = os.getenv("TELEGRAM_BOT_TOKEN")
    if not token:
        logger.error("TELEGRAM_BOT_TOKEN не задан")
        return

    ids_raw = os.getenv("TELEGRAM_CHAT_IDS", "")
    chat_ids = [cid.strip() for cid in ids_raw.split(",") if cid.strip()]
    if not chat_ids:
        logger.error("TELEGRAM_CHAT_IDS не задан или пуст")
        return

    bot = telegram.Bot(token=token)
    for cid in chat_ids:
        try:
            await bot.send_photo(
                chat_id=cid,
                photo=image_bytes,
                caption=caption,
                parse_mode=ParseMode.MARKDOWN_V2,
            )
            logger.info("Фото отправлено в chat_id=%s", cid)
        except telegram.error.TelegramError as e:
            logger.error("Ошибка Telegram send_photo для %s: %s", cid, e)

def escape_markdown_v2(text: str) -> str:
    """
    Экранирует ВСЕ специальные символы для Telegram MarkdownV2.
    """
    # Список символов, которые нужно экранировать в MarkdownV2
    escape_chars = r'_*[]()~`>#+-=|{}.!'
    # Обрабатываем обратный слэш отдельно, чтобы избежать SyntaxError
    return ''.join(f'\\{char}' if char in escape_chars else char for char in str(text)) 
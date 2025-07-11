"""scanner.py

Упрощённая логика анализа одной пары (только MACD):
• запрашиваем дневные свечи через data_provider.get_ohlcv_data()
• вычисляем MACD
• проверяем пересечение нулевой линии снизу вверх
• возвращаем dict с данными при выполнении условий, иначе None
"""
from __future__ import annotations

import logging
from typing import Dict, Optional

import pandas as pd
import ta

from data_provider import get_ohlcv_data

logger = logging.getLogger(__name__)

# --- Минимальные требования ------------------------------------------------
MIN_OHLC_ROWS = 40

# ---------------------------------------------------------------------------

def analyze_pair(mint_address: str) -> Optional[Dict[str, object]]:
    """Анализирует одну пару по её mint-адресу (только MACD).

    Args:
        mint_address: Mint токена на Solana.

    Returns:
        dict при срабатывании MACD-сигнала или None, если условия не выполнены / данных мало.
    """
    df = get_ohlcv_data(mint_address, days=60)
    if df.empty or len(df) < MIN_OHLC_ROWS:
        logger.info("Недостаточно данных для %s: %d строк (нужно мин. %d)", 
                   mint_address, len(df), MIN_OHLC_ROWS)
        return None
    
    logger.info("Получено %d дней данных для %s, анализируем MACD...", len(df), mint_address)

    # Расчёт MACD ---------------------------------------------------------
    close = df["Close"].astype(float)
    macd_indicator = ta.trend.MACD(close=close, window_slow=26, window_fast=12, window_sign=9)
    df["MACD"] = macd_indicator.macd()

    # Проверка условия: пересечение нуля снизу вверх ---------------------
    if len(df) < 2:
        logger.debug("Недостаточно строк для проверки пересечения: %d", len(df))
        return None

    prev = df.iloc[-2]
    curr = df.iloc[-1]

    # Пропускаем, если MACD не рассчитан (NaN)
    if pd.isna(prev["MACD"]) or pd.isna(curr["MACD"]):
        logger.debug("MACD содержит NaN для %s", mint_address)
        return None

    # Основное условие: вчера < 0, сегодня >= 0
    macd_cross = prev["MACD"] < 0 and curr["MACD"] >= 0

    if macd_cross:
        logger.info("✅ MACD сигнал найден для %s: %.6g → %.6g", 
                   mint_address, prev["MACD"], curr["MACD"])
        return {
            "mint": mint_address,
            "date": curr["Date"],
            "close": curr["Close"],
            "macd_prev": prev["MACD"],
            "macd_curr": curr["MACD"],
            "volumeUSD": curr["VolumeUSD"],
        }

    # INFO-печать причин отказа с конкретными значениями
    logger.info("Нет MACD-пересечения для %s: %.6g → %.6g", 
                mint_address, prev["MACD"], curr["MACD"])
    return None 
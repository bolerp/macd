"""data_provider.py

Клиент для Bitquery GraphQL-API и вспомогательные функции:
1. get_target_pairs()               – получить список токенов/пар по базовым фильтрам объёма.
2. check_liquidity(token_mint)      – убедиться, что у токена есть пул с TVL > threshold.
3. get_ohlcv_data(token_mint, ...)  – выгрузить дневные свечи (OHLCV) за N дней.

Все запросы синхронные (requests). При необходимости легко
перевести на httpx.AsyncClient – сигнатуры функций не изменятся.
"""
from __future__ import annotations

import os
import datetime as dt
import logging
from typing import Any, Dict, List, Optional

import requests
import pandas as pd

logger = logging.getLogger(__name__)

# --- Константы Bitquery ----------------------------------------------------
BITQUERY_ENDPOINT = "https://streaming.bitquery.io/eap"

_WSOLA_MINT = "So11111111111111111111111111111111111111112"  # Wrapped SOL

# ---------------------------------------------------------------------------

# ---------------------------------------------------------------------------
# Вспомогательная функция: выполнить GraphQL-запрос
# ---------------------------------------------------------------------------

def _execute_bitquery(query: str, variables: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    """Отправляет POST-запрос к Bitquery и возвращает JSON-payload (dict).

    Args:
        query: Строка GraphQL-запроса.
        variables: Словарь переменных, передаваемых в запрос.
    """
    token = os.getenv("BITQUERY_API_KEY")
    if not token:
        raise RuntimeError("Переменная окружения BITQUERY_API_KEY не установлена")

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {token}",
    }

    payload = {"query": query, "variables": variables or {}}

    try:
        response = requests.post(BITQUERY_ENDPOINT, json=payload, headers=headers, timeout=60)
        response.raise_for_status()
        data = response.json()
    except Exception as exc:
        logger.exception("Ошибка при обращении к Bitquery: %s", exc)
        raise

    # Bitquery оборачивает ошибки в key "errors"
    if "errors" in data:
        raise RuntimeError(f"Bitquery error: {data['errors']}")

    return data.get("data", {})


# ---------------------------------------------------------------------------
# 1. Получить список потенциальных пар
# ---------------------------------------------------------------------------

def get_target_pairs(
    volume_min_usd: int = 10_000,
    limit: int = 100,
    protocol_family: str = "Raydium",
    since_days: int = 30,
    name_like: str = "%pump",
) -> List[Dict[str, Any]]:
    """Возвращает список пар, удовлетворяющих фильтрам.

    Returns list of dicts:
        [
            {
                'marketAddress': str,
                'symbol': str,
                'name': str,
                'volumeUSD': float,
            },
            ...
        ]
    """
    since_date = (dt.datetime.utcnow() - dt.timedelta(days=since_days)).strftime("%Y-%m-%dT00:00:00Z")

    query = f"""
    query GetActivePumpTradingPairsComplete {{
      Solana {{
        DEXTradeByTokens(
          where: {{
            Trade: {{
              Dex: {{ ProtocolFamily: {{is: \"{protocol_family}\"}} }}
              Side: {{ AmountInUSD: {{gt: \"{volume_min_usd}\"}} }}
              Currency: {{ MintAddress: {{likeCaseInsensitive: \"{name_like}\"}} }}
            }}
            Block: {{ Time: {{since: \"{since_date}\"}} }}
            Transaction: {{ Result: {{Success: true}} }}
          }}
          limit: {{count: {limit}}}
          orderBy: {{descendingByField: \"volume\"}}
        ) {{
          Trade {{
            Market {{ MarketAddress }}
            Currency {{ MintAddress Symbol Name }}
          }}
          volume: sum(of: Trade_Side_AmountInUSD)
        }}
      }}
    }}
    """

    data = _execute_bitquery(query)
    results: List[Dict[str, Any]] = []
    pairs = data.get("Solana", {}).get("DEXTradeByTokens", [])
    for item in pairs:
        trade = item.get("Trade", {})
        market = trade.get("Market", {})
        currency = trade.get("Currency", {})
        results.append(
            {
                "marketAddress": market.get("MarketAddress"),
                "symbol": currency.get("Symbol"),
                "name": currency.get("Name"),
                "mintAddress": currency.get("MintAddress"),
                "volumeUSD": float(item.get("volume", 0)) if item.get("volume") else None,
            }
        )
    return results


# ---------------------------------------------------------------------------
# 2. Проверка ликвидности пула
# ---------------------------------------------------------------------------

def check_liquidity(token_mint: str, tvl_min_usd: int = 15_000) -> bool:
    """Возвращает True, если у токена есть пул с TVL (Quote_PostAmountInUSD) > tvl_min_usd."""

    query = """
    query CheckLiquidityForTokenByMint($tokenAddress: String!, $tvlMin: String!) {
      Solana {
        DEXPools(
          where: {
            Pool: {
              Market: { BaseCurrency: { MintAddress: {is: $tokenAddress} } }
              Quote: { PostAmountInUSD: {gt: $tvlMin} }
            }
            Transaction: { Result: {Success: true} }
            Block: { Time: {since: \"2025-07-01T00:00:00Z\"} }
          }
          limit: {count: 1}
          orderBy: {descendingByField: \"Pool_Quote_PostAmountInUSD\"}
        ) {
          Pool { Quote { PostAmountInUSD } }
        }
      }
    }
    """

    variables = {"tokenAddress": token_mint, "tvlMin": str(tvl_min_usd)}
    data = _execute_bitquery(query, variables)
    pools = data.get("Solana", {}).get("DEXPools", [])
    return len(pools) > 0


# ---------------------------------------------------------------------------
# 3. Дневные свечи OHLCV
# ---------------------------------------------------------------------------

def get_ohlcv_data(
    token_mint: str,
    quote_mint: str = _WSOLA_MINT,
    days: int = 60,
) -> pd.DataFrame:
    """Возвращает DataFrame с дневными свечами.

    Columns: Date, Open, High, Low, Close, Volume, VolumeUSD
    """
    since_date = (dt.datetime.utcnow() - dt.timedelta(days=days)).strftime("%Y-%m-%dT00:00:00Z")

    query = """
    query GetDailyOHLCFixed($baseMint: String!, $quoteMint: String!, $since: DateTime!, $limit: Int!) {
      Solana(dataset: combined) {
        DEXTradeByTokens(
          orderBy: {ascendingByField: \"Block_Timefield\"}
          where: {
            Trade: {
              Currency: { MintAddress: {is: $baseMint} }
              Side: { Currency: { MintAddress: {is: $quoteMint} } }
              PriceInUSD: {gt: 0}
            }
            Block: { Time: {since: $since} }
            Transaction: { Result: {Success: true} }
          }
          limit: {count: $limit}
        ) {
          Block { Timefield: Time(interval: {count: 1, in: days}) }
          volume: sum(of: Trade_Amount)
          volumeUSD: sum(of: Trade_Side_AmountInUSD)
          Trade {
            high: PriceInUSD(maximum: Trade_PriceInUSD)
            low: PriceInUSD(minimum: Trade_PriceInUSD)
            open: PriceInUSD(minimum: Block_Slot)
            close: PriceInUSD(maximum: Block_Slot)
          }
        }
      }
    }
    """
    variables = {
        "baseMint": token_mint,
        "quoteMint": quote_mint,
        "since": since_date,
        "limit": days + 5,  # небольшой запас
    }

    data = _execute_bitquery(query, variables)
    trades = data.get("Solana", {}).get("DEXTradeByTokens", [])
    if not trades:
        return pd.DataFrame()

    # Преобразуем в DataFrame
    records = []
    for item in trades:
        block_time = item["Block"]["Timefield"]
        trade = item["Trade"]
        records.append(
            {
                "Date": pd.to_datetime(block_time),
                "Open": float(trade["open"]),
                "High": float(trade["high"]),
                "Low": float(trade["low"]),
                "Close": float(trade["close"]),
                "Volume": float(item.get("volume", 0)),
                "VolumeUSD": float(item.get("volumeUSD", 0)),
            }
        )

    df = pd.DataFrame.from_records(records)
    df.sort_values("Date", inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df 
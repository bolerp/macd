# test_bitquery.py
from dotenv import load_dotenv
from data_provider import get_target_pairs, check_liquidity, get_ohlcv_data

load_dotenv()

pairs = get_target_pairs(limit=5)
print(pairs[:2])

mint = pairs[0]["mintAddress"]          # Берём mint, а не market
has_liquidity = check_liquidity(mint)
print("liquidity:", has_liquidity)

df = get_ohlcv_data(mint, days=10)
print(df.head())

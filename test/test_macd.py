"""test_macd.py

Тест-скрипт для проверки MACD расчётов на конкретном токене.
Использование: python test_macd.py <mint_address> [--days 90] [--from 2025-06-20] [--to 2025-06-30]

Пример: python test_macd.py 9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump --days 90 --from 2025-06-20
"""
import sys
import pandas as pd
import ta
from datetime import datetime, timedelta
from dotenv import load_dotenv
from data_provider import get_ohlcv_data

def test_macd(mint_address: str, days: int = 60, date_from: str = None, date_to: str = None):
    """Тестирует MACD расчёты для указанного токена."""
    
    print(f"🔍 Тестируем MACD для токена: {mint_address}")
    print(f"📊 Загружаем OHLCV данные за {days} дней...")
    
    # Получаем данные
    df = get_ohlcv_data(mint_address, days=days)
    if df.empty:
        print("❌ Не удалось получить данные для этого токена")
        return
    
    print(f"✅ Получено {len(df)} дневных свечей")
    print(f"📅 Период: {df['Date'].min()} → {df['Date'].max()}")
    print()
    
    # Рассчитываем MACD
    close = df["Close"].astype(float)
    macd_indicator = ta.trend.MACD(close=close, window_slow=26, window_fast=12, window_sign=9)
    
    df["MACD"] = macd_indicator.macd()
    df["MACD_Signal"] = macd_indicator.macd_signal()
    df["MACD_Histogram"] = macd_indicator.macd_diff()
    
    # Фильтруем по датам если указаны
    display_df = df.copy()
    if date_from:
        try:
            from_date = pd.to_datetime(date_from)
            display_df = display_df[display_df['Date'] >= from_date]
            print(f"🔍 Фильтр с: {date_from}")
        except:
            print(f"❌ Неверный формат даты 'от': {date_from}")
    
    if date_to:
        try:
            to_date = pd.to_datetime(date_to) + timedelta(days=1)  # включаем указанный день
            display_df = display_df[display_df['Date'] < to_date]
            print(f"🔍 Фильтр до: {date_to}")
        except:
            print(f"❌ Неверный формат даты 'до': {date_to}")
    
    if date_from or date_to:
        print()
    
    # Показываем отфильтрованные значения
    print(f"📈 MACD данные ({len(display_df)} дней):")
    print("-" * 90)
    
    for idx, row in display_df.iterrows():
        date = row["Date"].strftime("%Y-%m-%d")
        close_price = f"{row['Close']:.8g}"
        macd = f"{row['MACD']:.6g}" if pd.notna(row["MACD"]) else "NaN"
        signal = f"{row['MACD_Signal']:.6g}" if pd.notna(row["MACD_Signal"]) else "NaN"
        histogram = f"{row['MACD_Histogram']:.6g}" if pd.notna(row["MACD_Histogram"]) else "NaN"
        
        print(f"{date} | Close: {close_price:>12} | MACD: {macd:>10} | Signal: {signal:>10} | Hist: {histogram:>10}")
    
    # Анализ пересечений нулевой линии
    print()
    print("🎯 Анализ пересечений нулевой линии:")
    print("-" * 60)
    
    crossings = []
    
    for i in range(1, len(df)):
        prev_macd = df.iloc[i-1]["MACD"]
        curr_macd = df.iloc[i]["MACD"]
        curr_date = df.iloc[i]["Date"]
        
        if pd.notna(prev_macd) and pd.notna(curr_macd):
            if prev_macd < 0 and curr_macd >= 0:
                crossings.append((curr_date, "🟢 Пересечение вверх (BUY сигнал)", prev_macd, curr_macd))
            elif prev_macd > 0 and curr_macd <= 0:
                crossings.append((curr_date, "🔴 Пересечение вниз (SELL сигнал)", prev_macd, curr_macd))
    
    if crossings:
        for date, signal, prev_val, curr_val in crossings:
            print(f"{date.strftime('%Y-%m-%d')}: {signal}")
            print(f"    └─ {prev_val:.6g} → {curr_val:.6g}")
    else:
        print("Пересечений нулевой линии за весь период не обнаружено")
    
    # Текущее состояние
    print()
    print("📊 Текущее состояние (последний день):")
    print("-" * 40)
    last_row = df.iloc[-1]
    current_macd = last_row["MACD"]
    
    if pd.notna(current_macd):
        status = "🟢 ВЫШЕ нуля" if current_macd > 0 else "🔴 НИЖЕ нуля"
        print(f"MACD: {current_macd:.6g} ({status})")
        
        # Проверяем условие для сигнала (если есть предыдущий день)
        if len(df) >= 2:
            prev_macd = df.iloc[-2]["MACD"]
            if pd.notna(prev_macd):
                would_trigger = prev_macd < 0 and current_macd >= 0
                trigger_status = "✅ ДА" if would_trigger else "❌ НЕТ"
                print(f"Бычий сигнал (вчера < 0, сегодня >= 0): {trigger_status}")
    else:
        print("MACD: NaN (недостаточно данных)")

def main():
    load_dotenv()
    
    if len(sys.argv) < 2:
        print("Использование: python test_macd.py <mint_address> [--days 90] [--from 2025-06-20] [--to 2025-06-30]")
        print("Пример: python test_macd.py 9BB6NFEcjBCtnNLFko2FqVQBq8HHM13kCyYcdQbgpump --from 2025-06-20")
        return
    
    mint_address = sys.argv[1]
    
    # Парсим аргументы
    days = 60
    date_from = None
    date_to = None
    
    args = sys.argv[2:]
    i = 0
    while i < len(args):
        if args[i] == '--days' and i + 1 < len(args):
            days = int(args[i + 1])
            i += 2
        elif args[i] == '--from' and i + 1 < len(args):
            date_from = args[i + 1]
            i += 2
        elif args[i] == '--to' and i + 1 < len(args):
            date_to = args[i + 1]
            i += 2
        else:
            i += 1
    
    test_macd(mint_address, days, date_from, date_to)

if __name__ == "__main__":
    main() 
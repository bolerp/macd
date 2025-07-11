"""
chart_utils.py  –  делаем свечной график + MACD (тёмная тема, белый текст).

Функции:
    generate_chart(mint, symbol, days=90) -> bytes | None
"""

import io
from typing import Optional

import pandas as pd
import mplfinance as mpf
import matplotlib.pyplot as plt
import matplotlib.dates as md
from ta.trend import MACD

from data_provider import get_ohlcv_data


def _calc_macd(df: pd.DataFrame) -> pd.DataFrame:
    macd = MACD(df["Close"], window_slow=26, window_fast=12, window_sign=9)
    df["MACD"] = macd.macd()
    df["MACD_Signal"] = macd.macd_signal()
    return df


def _make_chart(df: pd.DataFrame, symbol: str) -> bytes:
    df_plot = df.tail(50).copy().set_index("Date")          # последние 50 дней

    style = mpf.make_mpf_style(
        base_mpf_style="binance",
        marketcolors=mpf.make_marketcolors(
            up="#26a69a",
            down="#ef5350",
            wick={"up": "#26a69a", "down": "#ef5350"},
            edge={"up": "#26a69a", "down": "#ef5350"},
        ),
        facecolor="#141518",
        figcolor="#141518",
        gridstyle="--",
        rc={
            "axes.grid": True,
            "grid.color": "#444444",
            "grid.alpha": 0.25,
            "font.size": 12,
            "text.color": "white",
            "axes.labelcolor": "white",
            "xtick.color": "white",
            "ytick.color": "white",
            "axes.edgecolor": "white",
        },
    )

    hist = df_plot["MACD"] - df_plot["MACD_Signal"]
    colors = ["#26a69a" if v >= 0 else "#ef5350" for v in hist]

    addplots = [
        mpf.make_addplot(hist, panel=1, type="bar", color=colors, alpha=0.5, ylabel="MACD"),
        mpf.make_addplot(df_plot["MACD"], panel=1, color="#2196f3", width=1.2),
        mpf.make_addplot(df_plot["MACD_Signal"], panel=1, color="#ffa726", width=1.2),
        mpf.make_addplot([0] * len(df_plot), panel=1, color="#888888", width=1, linestyle="--"),
    ]

    fig, axes = mpf.plot(
        df_plot,
        type="candle",
        style=style,
        addplot=addplots,
        panel_ratios=(3, 1.5),
        volume=False,
        ylabel="Price ($)",
        tight_layout=True,
        returnfig=True,
        figsize=(14, 8),
        title="",
    )

    # ──────────────────────────────────────────────────────────────
    #  ➜  Ограничиваем ось Y (цена) по перцентилям, чтобы шпильки
    #      не «сжимали» график.  95-й и 5-й перцентили → гибко для
    #      любых токенов.
    ax_price = axes[0]
    # --- устойчивая шкала без выбросов ------------------------
    q1 = df_plot["High"].quantile(0.25)
    q3 = df_plot["High"].quantile(0.75)
    iqr = q3 - q1

    upper = q3 + 1.5 * iqr           # верхний предел по Tukey
    lower = max(df_plot["Low"].min(), q1 - 1.5 * iqr)

    ax_price.set_ylim(lower * 0.98, upper * 1.02)

    # единый заголовок – выводим над рамкой, поэтому немного сдвигаем область графика вниз
    fig.subplots_adjust(top=0.90)
    fig.text(0.5, 0.94, f"{symbol} — Last 50 Days (MACD Signal)",
             ha="center", va="bottom",
             color="white", fontsize=14, weight="bold",
             transform=fig.transFigure)

    # красивые даты
    locator = md.AutoDateLocator(minticks=5, maxticks=8)
    fmt = md.DateFormatter("%d %b")
    for ax in (axes[0], axes[2]):
        ax.xaxis.set_major_locator(locator)
        ax.xaxis.set_major_formatter(fmt)
        ax.tick_params(axis="x", rotation=45)

    buf = io.BytesIO()
    fig.savefig(buf, format="png", dpi=120, bbox_inches="tight", facecolor="#141518")
    plt.close(fig)
    buf.seek(0)
    return buf.getvalue()


def generate_chart(mint: str, symbol: str, days: int = 90) -> Optional[bytes]:
    """
    Забирает OHLCV, рассчитывает MACD, рисует график.
    Возвращает bytes PNG или None, если данных нет.
    """
    df = get_ohlcv_data(mint, days=days)
    if df.empty:
        return None
    df = _calc_macd(df)
    return _make_chart(df, symbol) 
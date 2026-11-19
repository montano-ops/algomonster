"""OHLC data acquisition and validation for AlgoMonster.

Design notes
------------
- yfinance is the initial source (no API key). Its 15-minute history is limited to
  ~60 days by Yahoo Finance — callers must handle short samples.
- FX ``Volume`` from yfinance is *tick volume*, not traded volume. It is kept for
  completeness but must not be used as a liquidity/VWAP input.
- All functions are pure pandas operations (vectorised) and raise clear errors
  instead of silently returning empty frames.
"""
from __future__ import annotations

import pandas as pd

REQUIRED_COLUMNS = ["Open", "High", "Low", "Close", "Volume"]


def download_ohlc(
    ticker: str = "EURUSD=X",
    period: str = "60d",
    interval: str = "15m",
) -> pd.DataFrame:
    """Download OHLC candles via yfinance.

    Parameters
    ----------
    ticker: Yahoo ticker (``EURUSD=X`` for EUR/USD spot).
    period: yfinance period string. For ``interval="15m"`` the maximum is ``"60d"``.
    interval: candle interval, e.g. ``"15m"``.

    Returns
    -------
    DataFrame indexed by timestamp (UTC) with columns Open/High/Low/Close/Volume.

    Raises
    ------
    RuntimeError if yfinance returns no rows (network, rate limit, or bad ticker).
    """
    import yfinance as yf  # local import so tests don't require yfinance

    df = yf.download(ticker, period=period, interval=interval, progress=False, auto_adjust=False)
    if df is None or len(df) == 0:
        raise RuntimeError(
            f"yfinance returned no data for ticker={ticker!r} period={period!r} "
            f"interval={interval!r}. Check network/rate limits, or try a shorter period."
        )
    # yfinance >=0.2 returns MultiIndex columns for a single ticker; flatten them.
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
    return df


def validate_ohlc(df: pd.DataFrame, expected_interval: str = "15min") -> pd.DataFrame:
    """Validate and clean an OHLC frame. Returns a cleaned copy.

    Checks: required columns, no duplicate timestamps, chronological order,
    positive prices, High >= max(Open, Close), Low <= min(Open, Close),
    no NaNs in OHLC. Timezone is normalised to UTC.
    """
    if df is None or len(df) == 0:
        raise ValueError("Input DataFrame is empty.")
    missing = [c for c in REQUIRED_COLUMNS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")

    out = df.copy()
    # Normalise index to UTC DatetimeIndex.
    if not isinstance(out.index, pd.DatetimeIndex):
        raise ValueError("Index must be a DatetimeIndex.")
    if out.index.tz is None:
        out.index = out.index.tz_localize("UTC")
    else:
        out.index = out.index.tz_convert("UTC")

    if out.index.duplicated().any():
        raise ValueError("Duplicate timestamps found.")
    if not out.index.is_monotonic_increasing:
        out = out.sort_index()

    ohlc = out[["Open", "High", "Low", "Close"]]
    if ohlc.isna().any().any():
        raise ValueError("NaNs found in OHLC columns.")
    if (ohlc <= 0).any().any():
        raise ValueError("Non-positive prices found in OHLC columns.")
    if ((out["High"] < out[["Open", "Close"]].max(axis=1)) | (out["Low"] > out[["Open", "Close"]].min(axis=1))).any():
        raise ValueError("OHLC inconsistency: High/Low do not bracket Open/Close.")
    return out


def add_returns(df: pd.DataFrame) -> pd.DataFrame:
    """Add simple returns, log returns and candle range (vectorised)."""
    import numpy as np

    out = df.copy()
    out["simple_return"] = out["Close"].pct_change()
    out["log_return"] = np.log(out["Close"] / out["Close"].shift(1))
    out["candle_range"] = out["High"] - out["Low"]
    out["candle_range_pct"] = out["candle_range"] / out["Open"]
    return out

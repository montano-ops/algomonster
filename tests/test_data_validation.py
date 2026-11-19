"""Unit tests for src/data/loader.py — run with `pytest tests/ -v`."""
import numpy as np
import pandas as pd
import pytest

from src.data.loader import add_returns, validate_ohlc


def _make_ohlc(n: int = 10) -> pd.DataFrame:
    idx = pd.date_range("2024-01-01", periods=n, freq="15min", tz="UTC")
    close = 1.10 + np.cumsum(np.random.default_rng(0).normal(0, 0.0005, n))
    df = pd.DataFrame(
        {
            "Open": close,
            "High": close + 0.0005,
            "Low": close - 0.0005,
            "Close": close,
            "Volume": np.full(n, 1000),
        },
        index=idx,
    )
    return df


def test_validate_accepts_clean_data():
    df = _make_ohlc()
    out = validate_ohlc(df)
    assert len(out) == len(df)
    assert out.index.tz is not None


def test_validate_rejects_duplicates():
    df = _make_ohlc()
    df = pd.concat([df, df.iloc[:1]])
    with pytest.raises(ValueError, match="Duplicate"):
        validate_ohlc(df)


def test_validate_rejects_nan():
    df = _make_ohlc()
    df.loc[df.index[0], "Close"] = np.nan
    with pytest.raises(ValueError, match="NaN"):
        validate_ohlc(df)


def test_validate_rejects_bad_high_low():
    df = _make_ohlc()
    df.loc[df.index[0], "High"] = df.loc[df.index[0], "Close"] - 1.0
    with pytest.raises(ValueError, match="OHLC"):
        validate_ohlc(df)


def test_add_returns_shapes():
    df = _make_ohlc(20)
    out = add_returns(df)
    assert out["simple_return"].iloc[0] != out["simple_return"].iloc[0]  # NaN first row
    assert (out["candle_range"] > 0).all()
    # log return ≈ simple return for tiny moves
    assert np.allclose(out["log_return"].dropna(), out["simple_return"].dropna(), atol=1e-6)

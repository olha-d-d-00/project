import pandas as pd
import numpy as np


def run_vwap_reversion_strategy(df: pd.DataFrame, vwap_window: int = 20, threshold: float = 0.01) -> pd.DataFrame:
    df = df.copy()
    df["cum_vol"] = df["volume"].cumsum()
    df["cum_vol_price"] = (df["close"] * df["volume"]).cumsum()
    df["vwap"] = df["cum_vol_price"] / df["cum_vol"]

    df["delta"] = (df["close"] - df["vwap"]) / df["vwap"]

    df["signal"] = 0
    df.loc[df["delta"] > threshold, "signal"] = -1  # ціна сильно вища — продаємо
    df.loc[df["delta"] < -threshold, "signal"] = 1  # ціна нижча — купуємо

    return df[["close", "vwap", "delta", "signal"]]
import pandas as pd

def run_sma_crossover(df: pd.DataFrame, fast: int = 5, slow: int = 20) -> pd.DataFrame:
    df = df.copy()
    df["price"] = df["close"]
    df["sma_fast"] = df["price"].rolling(fast).mean()
    df["sma_slow"] = df["price"].rolling(slow).mean()
    df["signal"] = 0
    df.loc[df.index[fast:], "signal"] = (
        df["sma_fast"][fast:] > df["sma_slow"][fast:]
    ).astype(int)
    return df[["price", "sma_fast", "sma_slow", "signal"]]

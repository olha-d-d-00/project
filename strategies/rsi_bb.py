import pandas as pd
import numpy as np
import ta

def run_rsi_bb_strategy(df, rsi_period=14, bb_window=20, bb_std=2):
    df = df.copy()
    df['price'] = df['close']

    # RSI
    df['rsi'] = ta.momentum.RSIIndicator(close=df['price'], window=rsi_period).rsi()

    # Bollinger Bands
    bb = ta.volatility.BollingerBands(close=df['price'], window=bb_window, window_dev=bb_std)
    df['bb_low'] = bb.bollinger_lband()
    df['bb_high'] = bb.bollinger_hband()

    # Buy: RSI < 30 and price < BB low
    # Sell: RSI > 70 and price > BB high
    df['signal'] = 0
    df.loc[(df['rsi'] < 30) & (df['price'] < df['bb_low']), 'signal'] = 1
    df.loc[(df['rsi'] > 70) & (df['price'] > df['bb_high']), 'signal'] = -1

    return df[['price', 'rsi', 'bb_low', 'bb_high', 'signal']]

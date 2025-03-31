import os
import pandas as pd
from core.data_loader import DataLoader
from strategies.sma_cross import run_sma_crossover
from strategies.rsi_bb import run_rsi_bb_strategy
from strategies.vwap_reversion import run_vwap_reversion_strategy
from core.backtester import run_backtest

# Створюємо директорію для результатів
os.makedirs("results", exist_ok=True)

# Завантаження оброблених даних
loader = DataLoader()
df = loader.load_parquet()

print()

# === Стратегія SMA ===
print("\n🚀 Обробка стратегії: SMA")
sma_df = pd.concat([
    run_sma_crossover(df[df["symbol"] == symbol].copy()).assign(symbol=symbol)
    for symbol in df["symbol"].unique()
])
sma_df.to_csv("results/sma_signals.csv", index=True)
print("✅ Сигнали SMA збережено в results/sma_signals.csv")
print("📊 сигнал\n", sma_df["signal"].value_counts())
run_backtest(sma_df, "sma")

# === Стратегія RSI + Bollinger Bands ===
print("\n🚀 Обробка стратегії: RSI + Bollinger Bands")
rsi_bb_df = pd.concat([
    run_rsi_bb_strategy(df[df["symbol"] == symbol].copy()).assign(symbol=symbol)
    for symbol in df["symbol"].unique()
])
rsi_bb_df.to_csv("results/rsi_bb_signals.csv", index=True)
print("✅ Сигнали RSI + BB збережено в results/rsi_bb_signals.csv")
print("📊 Сигнали RSI + BB (Buy/Sell):\n", rsi_bb_df["signal"].value_counts())
run_backtest(rsi_bb_df, "rsi_bb")

# === Стратегія VWAP Reversion ===
print("\n🚀 Обробка стратегії: VWAP Reversion")
vwap_df = pd.concat([
    run_vwap_reversion_strategy(df[df["symbol"] == symbol].copy()).assign(symbol=symbol)
    for symbol in df["symbol"].unique()
])
vwap_df.to_csv("results/vwap_reversion_signals.csv", index=True)
print("✅ Сигнали VWAP збережено в results/vwap_reversion_signals.csv")
print("📊 Сигнали VWAP (Buy/Sell):\n", vwap_df["signal"].value_counts())
run_backtest(vwap_df, "vwap_reversion")
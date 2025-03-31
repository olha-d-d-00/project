import os
import pandas as pd

class DataLoader:
    def __init__(self, csv_folder="data/csv"):
        self.csv_folder = csv_folder
        self.parquet_path = "data/combined_1m_100_pairs.parquet"

    def combine_csv_to_parquet(self):
        all_dfs = []
        for filename in os.listdir(self.csv_folder):
            if filename.endswith(".csv"):
                filepath = os.path.join(self.csv_folder, filename)
                try:
                    df = pd.read_csv(filepath, header=None, names=[
                        "timestamp", "open", "high", "low", "close", "volume",
                        "close_time", "quote_asset_volume", "number_of_trades",
                        "taker_buy_base_asset_volume", "taker_buy_quote_asset_volume", "ignore"
                    ])
                    df["datetime"] = pd.to_datetime(df["timestamp"], unit="us", errors="coerce")
                    df = df.dropna(subset=["datetime"])
                    df.set_index("datetime", inplace=True)
                    df["symbol"] = filename.split("-")[0]
                    df = df[["symbol", "open", "high", "low", "close", "volume"]]
                    all_dfs.append(df)
                    print(f"✅ Завантажено: {filename}")
                except Exception as e:
                    print(f"❌ Помилка з {filename}: {e}")

        if all_dfs:
            combined = pd.concat(all_dfs)
            combined.to_parquet(self.parquet_path)
            print(f"\n✅ Збережено в {self.parquet_path}")
        else:
            print("⚠️ Дані не зібрано")

    def load_parquet(self, path="data/combined_1m_100_pairs.parquet"):
        try:
            df = pd.read_parquet(path)
            print(f"📥 Завантаження з {path}")
            print(df.head())
            print(f"\n📊 Всього рядків: {len(df)}")
            print(f"🪙 Унікальні пари: {df['symbol'].nunique()}")
            return df
        except FileNotFoundError:
            print("❌ Parquet файл не знайдено")
            return pd.DataFrame()

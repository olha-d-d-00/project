import os
import pandas as pd
import vectorbt as vbt
import matplotlib.pyplot as plt
import plotly.io as pio

# Налаштуємо формат для збереження графіків у PNG
pio.kaleido.scope.default_format = "png"

# Змінна для керування збереженням PNG графіків
save_png = True  # Встановити True, щоб зберігати PNG графіки

def run_backtest(df: pd.DataFrame, strategy_name: str):
    # Створюємо директорії для збереження метрик і графіків
    metrics_dir = f"results/metrics"
    screenshots_dir = f"results/screenshots/{strategy_name}"
    os.makedirs(metrics_dir, exist_ok=True)
    os.makedirs(screenshots_dir, exist_ok=True)

    metrics = []

    # Проходимо по кожній торговій парі
    for symbol in df["symbol"].unique():
        pair_df = df[df["symbol"] == symbol].copy()

        # Якщо немає стовпця price, пропускаємо пару
        if "price" not in pair_df.columns:
            print(f"⚠️ Стовпець 'price' відсутній для пари {symbol}, пропускаємо...")
            continue

        # Якщо немає сигналів, пропускаємо пару
        if pair_df["signal"].abs().sum() == 0:
            continue

        print(f"📈 Обробка пари: {symbol}")

        # Дані для розрахунку сигналів
        price = pair_df["price"]
        signal = pair_df["signal"]
        entries = signal == 1  # Вхід при сигналі 1 (купити)
        exits = signal == -1  # Вихід при сигналі -1 (продати)

        # Створення портфеля на основі сигналів
        pf = vbt.Portfolio.from_signals(
            close=price,
            entries=entries,
            exits=exits,
            fees=0.001,  # Комісія
            slippage=0.001  # Сліпейдж
        )

        # Отримання статистики портфеля
        stats = pf.stats()
        stats["symbol"] = symbol
        metrics.append(stats)

        # Генерація графіків equity curve
        try:
            print(f"🖼️ Генерація графіка для {symbol}...")

            # Створення графіка
            fig = pf.plot()

            if save_png:  # Якщо збереження PNG увімкнено
                # Переведення графіка Plotly в Matplotlib для збереження
                fig_matplotlib = fig.to_image(format="png")  # Конвертуємо в зображення

                with open(f"{screenshots_dir}/{symbol}.png", "wb") as f:
                    f.write(fig_matplotlib)  # Збереження графіка як PNG
                print(f"✅ Графік для {symbol} збережено!")
            else:
                print(f"📂 Збереження графіка для {symbol} вимкнено.")
        except Exception as e:
            print(f"⚠️ Не вдалося зберегти графік для {symbol}: {e}")

    # Збереження метрик для стратегії
    if metrics:
        metrics_df = pd.DataFrame(metrics).set_index("symbol")
        metrics_path = f"{metrics_dir}/{strategy_name}_metrics.csv"
        metrics_df.to_csv(metrics_path)  # Збереження метрик у CSV
        print(f"✅ Збережено метрики в {metrics_path}")
    else:
        print("⚠️ Немає метрик для збереження")
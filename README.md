# Тестове завдання: Backtesting System (Python + VectorBT)

## 📌 Опис

Проєкт реалізує інфраструктуру для бек-тестингу торгових стратегій на 1-хвилинних OHLCV-даних Binance.  
Мета — створення масштабованої, модульної системи для аналізу портфеля з 100 криптопар до BTC за лютий 2025 року.

## 📁 Структура проєкту
project/
├── core/
│   ├── data_loader.py          # Завантаження і кешування 1m-даних
│   ├── backtester.py           # Запуск бек-тесту з VectorBT
│   └── metrics.py              # Розрахунок метрик (Sharpe, drawdown, тощо)
├── strategies/
│   ├── base.py                 # Абстрактний клас для стратегій
│   ├── sma_cross.py            # Стратегія перетину ковзних середніх (SMA)
│   ├── rsi_bb.py               # RSI < 30 з підтвердженням Bollinger Band
│   └── vwap_reversion.py       # Mean reversion до VWAP
├── tests/
│   ├── test_backtester.py      # Unit-тест для бек-тестера
│   └── test_strategies.py      # Unit-тести для стратегій
├── data/
│   ├── btc_1m_feb25.parquet    # Комбіновані дані для 100 пар, лютий 2025
│   └── csv/                    # Окремі CSV по кожній валютній парі (через LFS)
├── results/
│   ├── metrics.csv             # Зведені метрики по стратегіях
│   ├── sma_signals.csv         # (LFS) Сигнали SMA
│   ├── rsi_bb_signals.csv      # (LFS) Сигнали RSI+BB
│   ├── vwap_reversion_signals.csv # (LFS) Сигнали VWAP
│   └── screenshots/
│       └── strategy1_equity.png   # Графік equity для однієї стратегії
├── main.py                     # Основний скрипт запуску проєкту
├── requirements.txt            # Список залежностей (pip)
└── README.md                   # Цей файл — опис проєкту


## ⚙️ Як запустити

> Python 3.10+  
> Рекомендується створити віртуальне середовище:

```bash
python -m venv .venv
source .venv/bin/activate    # Linux/macOS
.\.venv\Scripts\activate     # Windows

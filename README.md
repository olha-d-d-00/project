# Тестове завдання: Backtesting System (Python + VectorBT)

# Опис

Проєкт реалізує інфраструктуру для бек-тестингу торгових стратегій на 1-хвилинних OHLCV-даних Binance.  
Мета — створення масштабованої, модульної системи для аналізу портфеля з 100 криптопар до BTC за лютий 2025 року.

# Структура проєкту
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



1. Встановіть залежності:
pip install -r requirements.txt

2. Запустіть проєкт:
python main.py


Реалізовані стратегії

Стратегія та	Опис
SMA Crossover -	Вхід при перетині короткої SMA з довгою
RSI + Bollinger Band -	Вхід при RSI < 30 та підтвердженні від нижньої межі BB
VWAP Reversion -	Mean reversion до VWAP при великому відхиленні


Результати
Метрики (Sharpe, Max Drawdown, Total Return тощо) — збережено в /results/metrics/
Сигнали по кожній стратегії — .csv (через Git LFS)
Графіки equity curve, heatmap — збережено у /results/screenshots/


Git LFS
Репозиторій використовує Git Large File Storage для файлів >100MB
Для коректного клонування:
git lfs install
git clone https://github.com/olha-d-d-00/project.git

Тестування
Базові unit-тести для кожної стратегії та бектестера:
pytest tests/

Інше
Код дотримується стандартів PEP8

Документація представлена у форматі docstrings

Архітектура модульна, легко масштабована під інші таймфрейми чи біржі







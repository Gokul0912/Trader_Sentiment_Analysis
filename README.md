# Trader Sentiment Analysis

An exploratory data analysis project that studies how Bitcoin Fear & Greed sentiment relates to trader behavior and performance on Hyperliquid trading data.

## What This Demonstrates

- Data cleaning and feature engineering
- Daily account-level aggregation
- Sentiment-regime comparison
- Trader segmentation by activity level
- Strategy recommendations from observed behavior
- Lightweight Streamlit dashboard

## Tech Stack

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Streamlit

## Analysis Flow

1. Load Fear & Greed index data and historical trader execution data.
2. Normalize dates and join each trade to the sentiment regime for that day.
3. Create behavior and performance features:
   - daily PnL
   - win rate
   - average trade size
   - trades per day
   - long/short bias
4. Compare Fear and Greed periods.
5. Segment traders by frequency.
6. Generate strategy signals for risk-aware behavior changes.

## Key Findings

- Greed days show higher upside but also higher variability.
- Fear days tend to produce more cautious behavior and lower activity.
- Frequent traders are more sensitive to sentiment shifts.
- Position sizing and trade frequency are important risk controls across regimes.

## Run Locally

```bash
pip install -r requirements.txt
jupyter notebook notebooks/analysis.ipynb
```

Run the dashboard:

```bash
streamlit run dashboard.py
```

## Outputs

```text
outputs/tables/performance_summary.csv
outputs/tables/dashboard_data.csv
```

## Portfolio Note

This project is analysis-focused rather than production software. The next upgrade would be adding reproducible pipeline scripts, validation checks, and a clearer model evaluation section.

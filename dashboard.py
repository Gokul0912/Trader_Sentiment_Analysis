import streamlit as st
import pandas as pd

# Load processed data
df = pd.read_csv("outputs/tables/dashboard_data.csv")

st.title("Trader Performance vs Market Sentiment")

# Sidebar filters
sentiment = st.selectbox(
    "Select Market Sentiment",
    options=df['classification'].unique()
)

cluster = st.selectbox(
    "Select Behavior Cluster",
    options=sorted(df['behavior_cluster'].unique())
)

filtered_df = df[
    (df['classification'] == sentiment) &
    (df['behavior_cluster'] == cluster)
]

# Summary metrics
st.subheader("Summary Metrics")
st.metric("Average Daily PnL", round(filtered_df['daily_pnl'].mean(), 2))
st.metric("Average Win Rate", round(filtered_df['win_rate'].mean(), 2))
st.metric("Average Trades per Day", round(filtered_df['trades_per_day'].mean(), 2))

# Cluster comparison
st.subheader("Cluster-level Performance")
cluster_perf = (
    df.groupby('behavior_cluster')['daily_pnl']
      .mean()
      .reset_index()
)

st.bar_chart(cluster_perf.set_index('behavior_cluster'))

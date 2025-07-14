import pandas as pd
from sklearn.ensemble import IsolationForest

# Load and merge both CSVs
strategy = pd.read_csv("data/strategy_positions.csv")
broker = pd.read_csv("data/broker_positions.csv")

# Group by symbol
s_group = strategy.groupby('symbol')[['quantity', 'pnl']].sum()
b_group = broker.groupby('symbol')[['quantity', 'pnl']].sum()

# Merge on symbol
merged = s_group.join(b_group, lsuffix='_strategy', rsuffix='_broker', how='outer').fillna(0)

# Calculate differences
merged['qty_diff'] = abs(merged['quantity_strategy'] - merged['quantity_broker'])
merged['pnl_diff'] = abs(merged['pnl_strategy'] - merged['pnl_broker'])

# Create feature set for ML
features = merged[['quantity_strategy', 'quantity_broker', 'pnl_strategy', 'pnl_broker', 'qty_diff', 'pnl_diff']]

# Train Isolation Forest
model = IsolationForest(contamination=0.05, random_state=42)
merged['anomaly_score'] = model.fit_predict(features)

# Filter out anomalies
risky = merged[merged['anomaly_score'] == -1]

# Save results
risky.to_csv("data/ml_risk_report.csv")

print("✅ ML-based risk report saved to data/ml_risk_report.csv")
print("🔍 Risky Symbols Detected:", risky.shape[0])

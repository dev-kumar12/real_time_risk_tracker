import pandas as pd

# Load data
strategy = pd.read_csv("data/strategy_positions.csv")
broker = pd.read_csv("data/broker_positions.csv")

# Group by symbol and sum
s_group = strategy.groupby('symbol')[['quantity', 'pnl']].sum()
b_group = broker.groupby('symbol')[['quantity', 'pnl']].sum()

# Join both tables on symbol
merged = s_group.join(b_group, lsuffix='_strategy', rsuffix='_broker', how='outer').fillna(0)

# Calculate deviation
merged['qty_diff'] = abs(merged['quantity_strategy'] - merged['quantity_broker'])
merged['pnl_diff'] = abs(merged['pnl_strategy'] - merged['pnl_broker'])

# Set thresholds
QTY_THRESHOLD = 10
PNL_THRESHOLD = 1000

# Flag risky rows
risky = merged[(merged['qty_diff'] > QTY_THRESHOLD) | (merged['pnl_diff'] > PNL_THRESHOLD)]

# Save risk report
risky.to_csv("data/risk_report.csv")

print("✅ Risk report saved as data/risk_report.csv")

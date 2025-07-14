import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()

# Load the ML-based risk report
df = pd.read_csv("data/ml_risk_report.csv")

print("✅ ML Risk report loaded")
print("🔢 Rows in report:", len(df))
print(df.head())

if df.empty:
    console.print("🎉 No anomalies found by ML model!", style="green")
else:
    df.reset_index(inplace=True)

    table = Table(title="🤖 ML-Based Risk Report - Real-Time Risk Tracker")

    table.add_column("Symbol", justify="left", style="cyan", no_wrap=True)
    table.add_column("Qty Diff", justify="right", style="yellow")
    table.add_column("PNL Diff", justify="right", style="magenta")
    table.add_column("Anomaly Risk", justify="center", style="bold")

    for _, row in df.iterrows():
        symbol = str(row['symbol'])
        qty_diff = row['qty_diff']
        pnl_diff = row['pnl_diff']

        # Severity logic
        if qty_diff > 50 or pnl_diff > 3000:
            severity = "[bold red]HIGH[/bold red]"
        elif qty_diff > 20 or pnl_diff > 1500:
            severity = "[orange1]MEDIUM[/orange1]"
        else:
            severity = "[green]LOW[/green]"

        table.add_row(
            symbol,
            str(round(qty_diff, 2)),
            str(round(pnl_diff, 2)),
            severity
        )

    console.print(table)

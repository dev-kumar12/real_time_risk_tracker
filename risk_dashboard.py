import pandas as pd
from rich.console import Console
from rich.table import Table

console = Console()

# Load CSV
df = pd.read_csv("data/risk_report.csv")
print("✅ Risk report loaded")
print("🔢 Rows in report:", len(df))
print(df.head())  # Print first 5 rows to verify

if df.empty:
    console.print("🎉 No risk found!", style="green")
else:
    df.reset_index(inplace=True)

    table = Table(title="🚨 Risk Report - Real-Time Risk Tracker")

    table.add_column("Symbol", justify="left", style="cyan", no_wrap=True)
    table.add_column("Qty Diff", justify="right", style="yellow")
    table.add_column("PNL Diff", justify="right", style="magenta")
    table.add_column("Risk Level", justify="center", style="bold")

    for _, row in df.iterrows():
        symbol = str(row['symbol'])
        qty_diff = row['qty_diff']
        pnl_diff = row['pnl_diff']

        # Decide risk severity
        if qty_diff > 50 or pnl_diff > 3000:
            risk_level = "[bold red]HIGH[/bold red]"
        elif qty_diff > 20 or pnl_diff > 1500:
            risk_level = "[orange1]MEDIUM[/orange1]"
        else:
            risk_level = "[green]LOW[/green]"

        table.add_row(
            symbol,
            str(round(qty_diff, 2)),
            str(round(pnl_diff, 2)),
            risk_level
        )

    console.print(table)

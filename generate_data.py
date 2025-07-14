import csv
import random
from datetime import datetime, timedelta
import os

os.makedirs("data", exist_ok=True)

symbols = ['NIFTY', 'BANKNIFTY', 'RELIANCE', 'INFY', 'TCS', 'SBIN', 'ITC', 'HDFC', 'ICICIBANK', 'ONGC']

def generate_positions(file_path, variation=False):
    now = datetime.now()
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['symbol', 'quantity', 'pnl', 'timestamp'])
        for i in range(10000):
            symbol = random.choice(symbols)
            qty = random.randint(-100, 100)
            if variation and random.random() < 0.1:
                qty += random.randint(-10, 10)  # introduce mismatch in 10% rows

            pnl = round(random.uniform(-5000, 5000), 2)
            ts = now - timedelta(seconds=random.randint(0, 3600))
            writer.writerow([symbol, qty, pnl, ts.strftime("%Y-%m-%d %H:%M:%S")])

generate_positions("data/strategy_positions.csv", variation=False)
generate_positions("data/broker_positions.csv", variation=True)

print("✅ Mock data generated in /data")

# 📊 Real-Time Risk Tracker (with ML Anomaly Detection)

A Python-based CLI dashboard that monitors trading position mismatches between strategy and broker records. Enhances decision-making by detecting both rule-based and ML-based trading anomalies.

---

## 🚀 Features

- ✅ Compare strategy vs. broker trade positions
- 📉 Detect risk using thresholds (`qty_diff`, `pnl_diff`)
- 🤖 Auto-detect hidden anomalies using Isolation Forest (ML)
- 📦 Auto-generate summary risk reports
- 📺 Beautiful CLI dashboards with `rich` library
- 🔎 Works with mock or real trade data

---

## 📂 Project Structure 
real_time_risk_tracker/
│
├── data/
│ ├── strategy_positions.csv # Mock strategy trade data
│ ├── broker_positions.csv # Mock broker trade data
│ ├── risk_report.csv # Rule-based mismatches
│ ├── ml_risk_report.csv # ML-based anomalies
│
├── generate_data.py # Creates large mock data
├── risk_tracker.py # Rule-based detection logic
├── risk_dashboard.py # CLI dashboard (rules)
├── ml_risk_detector.py # ML risk detector (IsolationForest)
├── ml_risk_dashboard.py # CLI dashboard (ML)
├── README.md

## Rule Based Tracker

python risk_tracker.py
python risk_dashboard.py

## un ML risk detector

python ml_risk_detector.py
python ml_risk_dashboard.py

## SAMPLE OUTPUT 

🚨 Risk Report - Real-Time Risk Tracker
┏━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━┳━━━━━━━━━━━┓
┃ Symbol   ┃ Qty Diff ┃ PNL Diff ┃ Risk Level┃
┣━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━╋━━━━━━━━━━━┫
┃ RELIANCE ┃ 12       ┃ 1050.25  ┃ LOW       ┃
┃ INFY     ┃ 51       ┃ 3000.10  ┃ HIGH      ┃
┗━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━┻━━━━━━━━━━━┛



-- 1. Fetch all trades with significant PNL deviation
SELECT * FROM trades WHERE ABS(expected_pnl - actual_pnl) > 1000;

-- 2. Orders with large quantity mismatch
SELECT * FROM orders WHERE ABS(expected_qty - actual_qty) > 50;

-- 3. Symbols with most mismatches
SELECT symbol, COUNT(*) AS mismatch_count
FROM trades
WHERE ABS(expected_pnl - actual_pnl) > 1000 OR ABS(expected_qty - actual_qty) > 50
GROUP BY symbol
ORDER BY mismatch_count DESC;

-- 4. Failed orders
SELECT * FROM orders WHERE status = 'FAILED';

-- 5. Orders with execution delay > 5 seconds
SELECT * FROM orders WHERE TIMESTAMPDIFF(SECOND, placed_time, execution_time) > 5;

-- 6. Reconcile expected vs actual per symbol
SELECT
  e.symbol,
  SUM(e.expected_qty) AS total_expected_qty,
  SUM(a.actual_qty) AS total_actual_qty,
  SUM(e.expected_qty) - SUM(a.actual_qty) AS qty_diff
FROM expected_positions e
JOIN actual_positions a ON e.symbol = a.symbol
GROUP BY e.symbol;

-- 7. High-risk trades (negative PNL)
SELECT * FROM trades WHERE pnl < -500;

-- 8. Most volatile instruments
SELECT symbol, MAX(pnl) - MIN(pnl) AS volatility
FROM trades
GROUP BY symbol
ORDER BY volatility DESC;

-- 9. Daily PNL Summary
SELECT trade_date, SUM(pnl) AS total_pnl
FROM trades
GROUP BY trade_date
ORDER BY trade_date;

-- 10. Error-prone symbols
SELECT symbol, COUNT(*) AS error_count
FROM logs
WHERE log_level = 'ERROR'
GROUP BY symbol
ORDER BY error_count DESC;

-- 11. Orders executed with 0 quantity
SELECT * FROM orders WHERE actual_qty = 0;

-- 12. Orders where side (buy/sell) doesn’t match
SELECT * FROM orders WHERE expected_side != actual_side;

-- 13. Top 5 symbols by loss
SELECT symbol, SUM(pnl) AS total_loss
FROM trades
GROUP BY symbol
HAVING total_loss < 0
ORDER BY total_loss ASC
LIMIT 5;

-- 14. Count of orders per status
SELECT status, COUNT(*) FROM orders GROUP BY status;

-- 15. PNL grouped by trader
SELECT trader_id, SUM(pnl) AS pnl_per_trader
FROM trades
GROUP BY trader_id;

-- 16. Trades without execution time
SELECT * FROM orders WHERE execution_time IS NULL;

-- 17. Compare average PNL by instrument type
SELECT instrument_type, AVG(pnl) AS avg_pnl
FROM trades
GROUP BY instrument_type;

-- 18. Ratio of successful to failed orders
SELECT
  (SELECT COUNT(*) FROM orders WHERE status = 'SUCCESS') / 
  (SELECT COUNT(*) FROM orders WHERE status = 'FAILED') AS success_failure_ratio;

-- 19. Orders with partial fills
SELECT * FROM orders WHERE actual_qty < expected_qty AND actual_qty > 0;

-- 20. Total PNL vs Expected PNL
SELECT
  SUM(expected_pnl) AS total_expected_pnl,
  SUM(actual_pnl) AS total_actual_pnl,
  SUM(actual_pnl) - SUM(expected_pnl) AS pnl_diff
FROM trades;

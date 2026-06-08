-- Query 1
SELECT COUNT(*) AS total_funds
FROM dim_fund;
-- Query 2
SELECT AVG(nav) AS average_nav
FROM fact_nav;
-- Query 3
SELECT transaction_type,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY transaction_type;
-- Query 4
SELECT state,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;
-- Query 5
SELECT scheme_name,
       expense_ratio_pct
FROM dim_fund
WHERE expense_ratio_pct < 1;
-- Query 6
SELECT scheme_name,
       expense_ratio_pct
FROM dim_fund
ORDER BY expense_ratio_pct DESC
LIMIT 10;
-- Query 7
SELECT AVG(amount_inr) AS avg_transaction_amount
FROM fact_transactions;
-- Query 8
SELECT transaction_type,
       SUM(amount_inr) AS total_amount
FROM fact_transactions
GROUP BY transaction_type;
-- Query 9
SELECT kyc_status,
       COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY kyc_status;
-- Query 10
SELECT state,
       SUM(amount_inr) AS total_investment
FROM fact_transactions
GROUP BY state
ORDER BY total_investment DESC
LIMIT 10;
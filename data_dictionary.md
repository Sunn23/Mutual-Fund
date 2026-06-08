# Data Dictionary

## Table: dim_fund

| Column Name       | Data Type | Description                                  |
| ----------------- | --------- | -------------------------------------------- |
| amfi_code         | INTEGER   | Unique AMFI code of the mutual fund scheme   |
| scheme_name       | TEXT      | Name of the mutual fund scheme               |
| fund_house        | TEXT      | Asset Management Company (AMC)               |
| category          | TEXT      | Fund category (Equity, Debt, Hybrid, etc.)   |
| expense_ratio_pct | REAL      | Expense ratio percentage charged by the fund |
| risk_grade        | TEXT      | Risk level of the fund                       |

---

## Table: fact_nav

| Column Name | Data Type | Description                   |
| ----------- | --------- | ----------------------------- |
| amfi_code   | INTEGER   | AMFI code of the scheme       |
| nav_date    | DATE      | Date of NAV record            |
| nav         | REAL      | Net Asset Value of the scheme |

---

## Table: fact_transactions

| Column Name      | Data Type | Description                         |
| ---------------- | --------- | ----------------------------------- |
| investor_id      | TEXT      | Unique investor identifier          |
| transaction_date | DATE      | Date of transaction                 |
| amfi_code        | INTEGER   | AMFI code of the scheme             |
| transaction_type | TEXT      | SIP, Lumpsum, or Redemption         |
| amount_inr       | REAL      | Transaction amount in Indian Rupees |
| state            | TEXT      | Investor state                      |
| city             | TEXT      | Investor city                       |
| kyc_status       | TEXT      | KYC verification status             |

---

## Table: fact_performance

| Column Name      | Data Type | Description                                |
| ---------------- | --------- | ------------------------------------------ |
| amfi_code        | INTEGER   | AMFI code of the scheme                    |
| return_1yr_pct   | REAL      | One-year return percentage                 |
| return_3yr_pct   | REAL      | Three-year return percentage               |
| return_5yr_pct   | REAL      | Five-year return percentage                |
| alpha            | REAL      | Alpha performance metric                   |
| beta             | REAL      | Beta risk metric                           |
| sharpe_ratio     | REAL      | Risk-adjusted return measure               |
| sortino_ratio    | REAL      | Downside risk-adjusted return measure      |
| max_drawdown_pct | REAL      | Maximum percentage decline from peak value |

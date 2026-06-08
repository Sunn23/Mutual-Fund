CREATE TABLE dim_fund (
    amfi_code INTEGER PRIMARY KEY,
    scheme_name TEXT,
    fund_house TEXT,
    category TEXT,
    expense_ratio_pct REAL,
    risk_grade TEXT
);

CREATE TABLE fact_nav (
    amfi_code INTEGER,
    nav_date DATE,
    nav REAL,
    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_transactions (
    investor_id TEXT,
    transaction_date DATE,
    amfi_code INTEGER,
    transaction_type TEXT,
    amount_inr REAL,
    state TEXT,
    city TEXT,
    kyc_status TEXT,
    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);

CREATE TABLE fact_performance (
    amfi_code INTEGER,
    return_1yr_pct REAL,
    return_3yr_pct REAL,
    return_5yr_pct REAL,
    alpha REAL,
    beta REAL,
    sharpe_ratio REAL,
    sortino_ratio REAL,
    max_drawdown_pct REAL,
    FOREIGN KEY (amfi_code)
        REFERENCES dim_fund(amfi_code)
);
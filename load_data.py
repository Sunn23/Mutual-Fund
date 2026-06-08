import pandas as pd
from sqlalchemy import create_engine

# Connect to database
engine = create_engine("sqlite:///bluestock_mf.db")

# -----------------
# DIM FUND
# -----------------

fund_df = pd.read_csv("data/raw/01_fund_master.csv")

fund_df = fund_df[
    [
        "amfi_code",
        "scheme_name",
        "fund_house",
        "category",
        "expense_ratio_pct",
        "risk_category"
    ]
]
fund_df = fund_df.rename(
    columns={
        "risk_category": "risk_grade"
    }
)

print(fund_df.columns)  

fund_df.to_sql(
    "dim_fund",
    engine,
    if_exists="append",
    index=False
)

print("dim_fund loaded")

# -----------------
# FACT NAV
# -----------------

nav_df = pd.read_csv("data/processed/clean_nav.csv")

nav_df = nav_df.rename(
    columns={"date": "nav_date"}
)

nav_df = nav_df[
    [
        "amfi_code",
        "nav_date",
        "nav"
    ]
]

nav_df.to_sql(
    "fact_nav",
    engine,
    if_exists="append",
    index=False
)

print("fact_nav loaded")

# -----------------
# FACT TRANSACTIONS
# -----------------

tx_df = pd.read_csv(
    "data/processed/clean_transactions.csv"
)

tx_df = tx_df[
    [
        "investor_id",
        "transaction_date",
        "amfi_code",
        "transaction_type",
        "amount_inr",
        "state",
        "city",
        "kyc_status"
    ]
]

tx_df.to_sql(
    "fact_transactions",
    engine,
    if_exists="append",
    index=False
)

print("fact_transactions loaded")

# -----------------
# FACT PERFORMANCE
# -----------------

perf_df = pd.read_csv(
    "data/processed/clean_performance.csv"
)

perf_df = perf_df[
    [
        "amfi_code",
        "return_1yr_pct",
        "return_3yr_pct",
        "return_5yr_pct",
        "alpha",
        "beta",
        "sharpe_ratio",
        "sortino_ratio",
        "max_drawdown_pct"
    ]
]

perf_df.to_sql(
    "fact_performance",
    engine,
    if_exists="append",
    index=False
)

print("fact_performance loaded")

print("\nAll tables loaded successfully!")
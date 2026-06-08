import pandas as pd

perf_df = pd.read_csv("data/raw/07_scheme_performance.csv")

print("Rows before:", len(perf_df))

# Remove duplicates
perf_df = perf_df.drop_duplicates()

# Ensure numeric columns are numeric
numeric_cols = [
    'return_1yr_pct',
    'return_3yr_pct',
    'return_5yr_pct',
    'benchmark_3yr_pct',
    'alpha',
    'beta',
    'sharpe_ratio',
    'sortino_ratio',
    'std_dev_ann_pct',
    'max_drawdown_pct',
    'expense_ratio_pct'
]

for col in numeric_cols:
    perf_df[col] = pd.to_numeric(perf_df[col], errors='coerce')

# Negative Sharpe Ratios
negative_sharpe = perf_df[perf_df['sharpe_ratio'] < 0]

print("\nNegative Sharpe Ratios:")
print(len(negative_sharpe))

# Expense Ratio Validation
invalid_expense = perf_df[
    (perf_df['expense_ratio_pct'] < 0.1) |
    (perf_df['expense_ratio_pct'] > 2.5)
]

print("\nInvalid Expense Ratios:")
print(len(invalid_expense))

# Check missing values
print("\nMissing Values:")
print(perf_df.isna().sum().sum())

print("\nRows after:", len(perf_df))

# Save cleaned file
perf_df.to_csv("data/processed/clean_performance.csv", index=False)

print("\nClean performance file saved.")
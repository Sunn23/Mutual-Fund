import pandas as pd

# Load data
tx_df = pd.read_csv("data/raw/08_investor_transactions.csv")

print("Rows before:", len(tx_df))

# Convert date
tx_df['transaction_date'] = pd.to_datetime(tx_df['transaction_date'])

# Standardize transaction type
tx_df['transaction_type'] = (
    tx_df['transaction_type']
    .str.strip()
    .str.title()
)

# Remove duplicates
tx_df = tx_df.drop_duplicates()

# Validate amount > 0
tx_df = tx_df[tx_df['amount_inr'] > 0]

# Check values
print("\nTransaction Types:")
print(tx_df['transaction_type'].unique())

print("\nKYC Status Values:")
print(tx_df['kyc_status'].unique())

print("\nInvalid Amounts:")
print((tx_df['amount_inr'] <= 0).sum())

print("\nDuplicate Rows:")
print(tx_df.duplicated().sum())

print("\nRows after:", len(tx_df))

# Save cleaned file
tx_df.to_csv("data/processed/clean_transactions.csv", index=False)

print("\nClean transactions file saved.")
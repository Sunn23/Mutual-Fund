import pandas as pd

# Load datasets
fund_master = pd.read_csv("data/raw/01_fund_master.csv")
nav_history = pd.read_csv("data/raw/02_nav_history.csv")

# Get unique AMFI codes
master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

# Find codes present in fund_master but missing in nav_history
missing_codes = master_codes - nav_codes

print("Total AMFI Codes in Fund Master:", len(master_codes))
print("Total AMFI Codes in NAV History:", len(nav_codes))
print("Missing AMFI Codes:", len(missing_codes))

if len(missing_codes) > 0:
    print("\nMissing Codes:")
    for code in sorted(missing_codes):
        print(code)
else:
    print("\nAll AMFI codes are present in NAV History.")

# Save report
report = pd.DataFrame({
    "missing_amfi_code": list(missing_codes)
})

report.to_csv(
    "report/amfi_validation_report.csv",
    index=False
)

print("\nReport saved to report/amfi_validation_report.csv")
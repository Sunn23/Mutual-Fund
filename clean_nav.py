import pandas as pd
nav_df = pd.read_csv("data/raw/02_nav_history.csv")
print("Rows before:", len(nav_df))
#Convert date column
nav_df['date'] = pd.to_datetime(nav_df['date'])
#Sort by fund and date
nav_df = nav_df.sort_values(['amfi_code', 'date'])
#Remove duplicates
nav_df = nav_df.drop_duplicates()
#Fill missing NAV values
nav_df['nav'] = nav_df.groupby('amfi_code')['nav'].ffill()
#Keep only positive NAVs
nav_df = nav_df[nav_df['nav'] > 0]
print("Rows after:", len(nav_df))
print("Remaining missing NAVs:", nav_df['nav'].isna().sum())
print("Remaining duplicates:", nav_df.duplicated().sum())
print("NAV <= 0:", (nav_df['nav'] <= 0).sum())
#Save cleaned file
nav_df.to_csv("data/processed/clean_nav.csv", index=False)
print("Clean file saved.")
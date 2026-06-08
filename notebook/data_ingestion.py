import pandas as pd
import os

folder = "data/raw"

for file in os.listdir(folder):
    if file.endswith(".csv"):
        file_path = os.path.join(folder, file)

        df = pd.read_csv(file_path)

        print("\n" + "=" * 50)
        print("File:", file)
        print("Shape:", df.shape)
        print("\nData Types:")
        print(df.dtypes)
        print("\nFirst 5 Rows:")
        print(df.head())
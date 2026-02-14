import pandas as pd
import os

# Get absolute path of this script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Build correct path to CSV
csv_path = os.path.join(BASE_DIR, "..", "data", "raw", "sales.csv")

# Read CSV
df = pd.read_csv(csv_path)

print("DATA EXTRACTED SUCCESSFULLY")
print(df.head())

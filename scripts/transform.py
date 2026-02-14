import pandas as pd
import os

# Base directory (scripts folder)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# File paths
input_path = os.path.join(BASE_DIR, "..", "data", "raw", "sales.csv")
output_path = os.path.join(BASE_DIR, "..", "data", "processed", "clean_sales.csv")

# Read raw data
df = pd.read_csv(input_path)

print("RAW SHAPE:", df.shape)

# 1. Remove duplicates
df = df.drop_duplicates()

# 2. Remove rows with missing values
df = df.dropna()

# 3. Convert Date column to proper date
df["Date"] = pd.to_datetime(
    df["Date"],
    errors="coerce",
    infer_datetime_format=True
)
df = df.dropna(subset=["Date"])


# 4. Standardize column names
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ", "_")
)

print("CLEANED SHAPE:", df.shape)

# Save cleaned data
df.to_csv(output_path, index=False)

print("CLEAN DATA SAVED TO processed/clean_sales.csv")

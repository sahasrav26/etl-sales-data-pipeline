import pandas as pd
import logging
import sys
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)

# Path to processed file
csv_path = "/opt/airflow/dags/data/processed/clean_sales.csv"

logging.info("Reading transformed data...")

df = pd.read_csv(csv_path)
logging.info(df.columns)


logging.info(f"Rows before validation: {len(df)}")

# ---- VALIDATION RULES ----

# 1️⃣ No null transactionno
if df["transactionno"].isnull().any():
    logging.error("Validation Failed: Null transactionno found.")
    sys.exit(1)

# 2️⃣ Quantity must be positive
if (df["quantity"] <= 0).any():
    logging.error("Validation Failed: Negative or zero quantity found.")
    sys.exit(1)

# 3️⃣ Price must be positive
if (df["price"] <= 0).any():
    logging.error("Validation Failed: Negative or zero price found.")
    sys.exit(1)

logging.info("Validation passed successfully.")

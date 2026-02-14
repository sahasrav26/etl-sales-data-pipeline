import pandas as pd
import os
from sqlalchemy import create_engine

# Get base directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Path to cleaned CSV
csv_path = os.path.join(BASE_DIR, "..", "data", "processed", "clean_sales.csv")

# Read cleaned data
df = pd.read_csv(csv_path)

print("ROWS TO LOAD:", len(df))

# PostgreSQL connection (CHANGE PASSWORD)
engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
)

# Load data
df.to_sql("sales", engine, if_exists="append", index=False)

print("DATA LOADED INTO POSTGRESQL SUCCESSFULLY")

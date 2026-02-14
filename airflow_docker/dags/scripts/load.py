import pandas as pd
import os
import logging
from sqlalchemy import create_engine

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(BASE_DIR, "..", "data", "processed", "clean_sales.csv")

logging.info("Reading cleaned data for loading...")

df = pd.read_csv(input_path)

logging.info(f"Rows to load: {len(df)}")

engine = create_engine(
    "postgresql+psycopg2://airflow:airflow@postgres:5432/airflow"
)

df.to_sql(
    "sales",
    engine,
    if_exists="append",
    index=False,
    chunksize=5000
)

logging.info("Data loaded successfully into PostgreSQL.")

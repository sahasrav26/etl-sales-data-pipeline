import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

input_path = os.path.join(BASE_DIR, "..", "data", "raw", "sales.csv")

logging.info("Reading raw sales data...")

df = pd.read_csv(input_path)

logging.info(f"Extracted rows: {len(df)}")

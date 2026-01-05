import time
import logging
from pathlib import Path
import pandas as pd

from src.extract import extract_transactions, load_schema
from src.transform import transform_transactions
from src.load import load_to_db

RAW_DATA_PATH = Path("data/raw/Retail_Transactions_Dataset_sample.csv")
SCHEMA_PATH = Path("data/raw/schema.json")
PROCESSED_DATA_PATH = Path("data/processed/Retail_Transactions_Dataset_clean.csv")
DB_PATH = Path("data/processed/retail_transactions.db")

LOG_PATH = Path("logs/etl_pipeline.log")
LOG_PATH.parent.mkdir(exist_ok=True)

logging.basicConfig(
    filename=LOG_PATH,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


def run_pipeline(retries=3, retry_delay=5):
    attempt = 1

    while attempt <= retries:
        try:
            logging.info("Starting ETL pipeline")

            schema = load_schema(SCHEMA_PATH)
            raw_df = extract_transactions(RAW_DATA_PATH, schema)
            logging.info(f"Extracted {len(raw_df)} rows")

            transformed_df = transform_transactions(raw_df)
            transformed_df.to_csv(PROCESSED_DATA_PATH, index=False)
            logging.info(f"Transformed {len(transformed_df)} rows")

            load_to_db(transformed_df, DB_PATH)
            logging.info("Loaded data into database")

            logging.info("ETL pipeline completed successfully")
            print("ETL pipeline completed successfully")
            return

        except Exception as e:
            logging.error(f"Pipeline failed on attempt {attempt}: {e}")
            print(f"Pipeline failed on attempt {attempt}: {e}")

            attempt += 1
            time.sleep(retry_delay)

    logging.critical("ETL pipeline failed after maximum retries")
    raise RuntimeError("ETL pipeline failed after maximum retries")


if __name__ == "__main__":
    run_pipeline()
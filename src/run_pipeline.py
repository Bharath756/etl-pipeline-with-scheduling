import sys
from pathlib import Path

# Add src directory to Python path
SRC_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SRC_DIR))

from extract import extract_transactions, load_schema
from transform import transform_transactions
from load import load_to_db


def run_pipeline():
    schema = load_schema("data/raw/schema.json")
    raw_df = extract_transactions("data/raw/Retail_Transactions_Dataset_sample.csv", schema)
    transformed_df = transform_transactions(raw_df)
    load_to_db(transformed_df, "data/processed/retail_transactions.db")
    print("ETL pipeline completed successfully")


if __name__ == "__main__":
    run_pipeline()
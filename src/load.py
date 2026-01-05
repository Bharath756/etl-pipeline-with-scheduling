import pandas as pd
import sqlite3
from pathlib import Path

DB_PATH = Path("data/processed/retail_transactions.db")
TABLE_NAME = "transactions"


def load_to_db(df: pd.DataFrame, db_path: Path):
    conn = sqlite3.connect(db_path)

    df.to_sql(
        TABLE_NAME,
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()


if __name__ == "__main__":
    df = pd.read_csv("data/processed/Retail_Transactions_Dataset_clean.csv")

    load_to_db(df, DB_PATH)

    print(f"Loaded {len(df)} rows into database table '{TABLE_NAME}'")

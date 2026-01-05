import pandas as pd
import json


def load_schema(schema_path: str) -> dict:
    with open(schema_path, "r") as f:
        return json.load(f)


def extract_transactions(csv_path: str, schema: dict) -> pd.DataFrame:
    df = pd.read_csv(csv_path)
    return df

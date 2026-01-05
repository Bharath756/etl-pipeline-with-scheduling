import pandas as pd


def transform_transactions(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and transform raw retail transaction data
    into analytics-ready format.
    """

    # Normalize column names
    df.columns = [col.strip().lower() for col in df.columns]

    # Parse datetime
    if "date" in df.columns:
        df["date"] = pd.to_datetime(df["date"], errors="coerce")

    # Remove rows with missing critical fields
    required_columns = ["transaction_id", "date", "total_items", "total_cost"]
    df = df.dropna(subset=[c for c in required_columns if c in df.columns])

    # Enforce numeric types
    df["total_items"] = pd.to_numeric(df["total_items"], errors="coerce")
    df["total_cost"] = pd.to_numeric(df["total_cost"], errors="coerce")

    # Business rules
    df = df[df["total_items"] > 0]
    df = df[df["total_cost"] > 0]

    # Normalize boolean field
    if "discount_applied" in df.columns:
        df["discount_applied"] = df["discount_applied"].astype(bool)

    # Trim string columns
    string_cols = df.select_dtypes(include="object").columns
    for col in string_cols:
        df[col] = df[col].str.strip()

    return df

if __name__ == "__main__":
    raw_df = pd.read_csv("data/raw/Retail_Transactions_Dataset_sample.csv")

    processed_df = transform_transactions(raw_df)

    processed_df.to_csv(
        "data/processed/Retail_Transactions_Dataset_clean.csv",
        index=False
    )

    print("Rows after transformation:", len(processed_df))

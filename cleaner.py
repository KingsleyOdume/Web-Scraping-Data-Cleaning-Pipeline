import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Clean raw scraped data into structured format."""
    if "price" in df.columns:
        df["price"] = df["price"].str.replace("£", "", regex=False)
        df["price"] = df["price"].str.replace("$", "", regex=False)
        df["price"] = df["price"].str.replace(",", "", regex=False)
        df["price"] = pd.to_numeric(df["price"], errors="coerce")

    # Drop duplicates
    df = df.drop_duplicates()

    # Handle missing values
    df = df.dropna()

    return df

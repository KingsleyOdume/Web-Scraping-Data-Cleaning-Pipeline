import sqlite3
import pandas as pd

DB_NAME = "scraped_data.db"

def save_to_sql(df: pd.DataFrame, table_name: str):
    """Save cleaned DataFrame into SQLite database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        df.to_sql(table_name, conn, if_exists="replace", index=False)
        conn.close()
        print("Data saved successfully to SQL.")
    except Exception as e:
        print(f"SQL Save Error: {e}")

def get_data_from_sql(table_name: str) -> pd.DataFrame:
    """Retrieve data from SQLite database."""
    try:
        conn = sqlite3.connect(DB_NAME)
        df = pd.read_sql(f"SELECT * FROM {table_name}", conn)
        conn.close()
        return df
    except Exception as e:
        print(f"SQL Load Error: {e}")
        return None

import streamlit as st
import pandas as pd
from scraper import scrape_products
from cleaner import clean_data
from database import save_to_sql, get_data_from_sql

st.set_page_config(page_title="Web Scraping & Data Cleaning Pipeline", layout="wide")

st.title("🌐 Web Scraping & Data Cleaning Pipeline")
st.write("Automate data collection, cleaning, and storage into SQL for dashboards.")

# Input URL
url = st.text_input("Enter website URL to scrape:", "https://books.toscrape.com/")

if st.button("Run Scraper"):
    with st.spinner("Scraping data..."):
        raw_data = scrape_products(url)
        if not raw_data:
            st.error("No data found! Check the website or scraper logic.")
        else:
            st.success(f"Scraped {len(raw_data)} records successfully!")

            # Show raw data
            st.subheader("📂 Raw Scraped Data")
            raw_df = pd.DataFrame(raw_data)
            st.dataframe(raw_df)

            # Clean data
            st.subheader("🧹 Cleaned Data")
            clean_df = clean_data(raw_df)
            st.dataframe(clean_df)

            # Save to SQL
            save_to_sql(clean_df, "scraped_table")

            st.success("✅ Data cleaned & saved to SQL database!")

# Load from SQL
if st.button("Load from Database"):
    df = get_data_from_sql("scraped_table")
    if df is not None:
        st.subheader("📊 Data from SQL Database")
        st.dataframe(df)
    else:
        st.error("No data found in database yet.")

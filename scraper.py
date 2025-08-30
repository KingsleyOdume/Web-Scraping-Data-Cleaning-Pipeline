import requests
from bs4 import BeautifulSoup

def scrape_products(url: str):
    """Scrape product data from a given URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        products = []
        for item in soup.find_all("article", class_="product_pod"):
            title = item.h3.a["title"]
            price = item.find("p", class_="price_color").text.strip()
            products.append({"title": title, "price": price})

        return products
    except Exception as e:
        print(f"Scraping error: {e}")
        return []

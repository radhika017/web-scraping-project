import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://books.toscrape.com"

response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")

books = []
prices = []

for item in soup.find_all("article", class_="product_pod"):

    title = item.h3.a["title"]

    price = item.find("p", class_="price_color").text

    books.append(title)
    prices.append(price)

data = pd.DataFrame({
    "Book Title": books,
    "Price": prices
})

print(data)

data.to_csv("books_data.csv", index=False)

print("Dataset Saved Successfully!")
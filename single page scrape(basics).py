import requests
from bs4 import BeautifulSoup

response = requests.get("https://books.toscrape.com")
response.encoding = "utf-8"
print(response.status_code)
#Printing all books and prices on Page 1
soup = BeautifulSoup(response.text, "html.parser")
titles = {}
books = soup.find_all("article", class_="product_pod")
for book in books:
    title = book.find("h3").find("a").get("title")
    price = book.find("div", class_="product_price").find("p", class_="price_color").text
    # in_stock = book.find("div", class_="product_price").find("p", class_="price_color")

    titles[title] = {
        "Price": str(price)
    }
    
for title, values in titles.items():
    print(f"{title} : {values["Price"]}")

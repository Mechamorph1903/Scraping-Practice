import requests
from bs4 import BeautifulSoup
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


count = 1
titles = []
while count <= 50:
    response = requests.get(f"https://books.toscrape.com/catalogue/page-{count}.html", verify=False)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "html.parser")
    
    books = soup.find_all("article", class_="product_pod")
    for book in books:
        title = book.find("h3").find("a").get("title")
        price = book.find("div", class_="product_price").find("p", class_="price_color").text
        # in_stock = book.find("div", class_="product_price").find("p", class_="price_color")

        titles.append({
            "Title": title,
            "Price": str(price)
        })
    count += 1
        

with open("books.txt", "w", encoding="utf-8") as f:
    f.write(f"The total Number of Books on the site is: {len(titles)}\n\n\n")
    f.write(f"I will output books by title and Price\n\n\n")
    for title in titles: 
        f.write(f"{title["Title"]}: {title["Price"]}\n")


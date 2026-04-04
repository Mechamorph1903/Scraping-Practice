from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# 1 - set up the browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run invisibly
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

count = 1
titles = []

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

while count <= 50:
	driver.get(f"https://books.toscrape.com/catalogue/page-{count}.html")
	response = driver.page_source
	soup = BeautifulSoup(response, "html.parser")
	books = soup.find_all("article", class_="product_pod")
	for book in books:
		title = book.find("h3").find("a").get("title")
		price = book.find("div", class_="product_price").find("p", class_="price_color").text
		in_stock = book.find("div", class_="product_price").find("p", class_="availability").text.strip() == "In stock"

		titles.append({
			"Title": title,
			"Price": str(price),
			"In Stock": in_stock
		})
	count += 1
driver.quit()

with open("selenium_books.txt", "w", encoding="utf-8") as f:
    f.write(f"The total Number of Books on the site is: {len(titles)}\n\n\n")
    f.write(f"I will output books by title and Price\n\n\n")
    for title in titles: 
        f.write(f"{title["Title"]}: {title["Price"]} - {"Book is Available" if title["In Stock"] else "Book Unavailable"}\n")
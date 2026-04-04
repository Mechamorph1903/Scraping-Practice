from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

# 1 - set up the browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # Runs Chrome without opening a visible window. Chrome does everything normally — loads pages, runs JavaScript, renders content — just invisibly in the background. Without this a Chrome window would pop up every time you run your script.
options.add_argument("--no-sandbox") # The sandbox is a Chrome security feature that isolates the browser from the rest of your system. On some Windows setups the sandbox causes crashes when Chrome is launched programmatically. This disables it. Safe to use for scraping on your own machine — you'd never disable this in a production web server though.
options.add_argument("--disable-dev-shm-usage") # /dev/shm is a shared memory location Chrome uses on Linux. On Windows this doesn't really apply but it can still cause memory errors when Chrome is run headlessly. This flag tells Chrome to use a different memory approach that's more stable in automated environments.
options.add_argument("--disable-gpu") # Disables GPU hardware acceleration. When running headlessly there's no screen so GPU rendering doesn't make sense anyway. Without this flag some Windows setups throw GPU-related errors because Chrome tries to use graphics hardware that isn't available in headless mode.
options.add_argument("--remote-debugging-port=9222") # Opens a port that allows external tools to connect to and inspect the running Chrome instance. Selenium uses this to communicate with the browser — send it instructions, read back results. Think of it as the phone line between your Python code and the Chrome browser. Without a working communication channel Selenium can't control Chrome at all, which was exactly the error you were getting.

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
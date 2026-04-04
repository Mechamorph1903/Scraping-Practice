from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import requests


# 1 - set up the browser
options = webdriver.ChromeOptions()
options.add_argument("--headless")  # run invisibly
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()),
    options=options
)

# 2 - go to a page
driver.get("https://books.toscrape.com")
print(f"Selenium HTML length: {len(driver.page_source)}")
print(f"Page title: {driver.title}")
# 3 - get the fully rendered HTML
html = driver.page_source

#requests version
response = requests.get("https://books.toscrape.com", verify=False)
print(f"requests HTML length: {len(response.text)}")


# 4 - always close the browser when done
driver.quit()

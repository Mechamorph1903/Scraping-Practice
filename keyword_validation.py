from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--no-sandbox") 
options.add_argument("--disable-dev-shm-usage") 
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

def scrapeJob(url):
	sehski = { # JSON data of 
		"Status": False,
		"Data": ""
		} 
		
	try:
	
		driver = webdriver.Chrome(
		service=Service(ChromeDriverManager().install()),
		options=options
		)
		

		driver.get(url)

		soup = BeautifulSoup(driver.page_source, "html.parser")
		jusText = soup.get_text()

		keywords = keywords = [
		# role related
		"candidate", "candidates", "hiring", "applicant", "applicants",
		"apply", "application", "opening", "vacancy", "vacancies", "position",
		
		# job details
		"salary", "compensation", "benefits", "bonus", "equity", "pay range",
		"full time", "part time", "contract", "remote", "hybrid", "on site",
		
		# location
		"location", "locations", "relocation", "based in", "office",
		
		# requirements
		"experience", "requirements", "qualifications", "skills", "responsibilities",
		"bachelor", "degree", "years of experience", "preferred", "required",
		
		# company language
		"team", "role", "opportunity", "join us", "we are looking",
		"about the role", "about us", "what you will do", "what we offer"
		]

		if any(word in jusText.lower() for word in keywords):
			print("This got one of the words innit")
			sehski["Status"] =  True
			sehski["Data"] = jusText
			#more logic
			return sehski
		else:
			print("This don't look like a job site big man")
			return sehski
	except Exception as e:
			print(f"Something went wrong with driver creation: {e}")
			return sehski
	finally:
		if driver:
			driver.quit()

	


scrapeJob("https://job-boards.greenhouse.io/figma/jobs/5691911004?gh_jid=5691911004&gh_src=28109e334us&source=LinkedIn")
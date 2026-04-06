# 🕷️ Scraping Practice

A hands-on scraping learning repository built April '26. This repo documents my journey learning web scraping from the ground up — starting with static pages, progressing to JavaScript-rendered sites, and ultimately combining scraping with AI to build something real.

---

## What's In Here

### `scraping_practice.py` — requests + BeautifulSoup
My first scraper. Fetches the [Books to Scrape](https://books.toscrape.com) practice site using `requests` and parses the HTML with `BeautifulSoup`. Scrapes all 20 books on the page including title and price.

**What I learned:**
- How `requests.get()` fetches raw HTML
- How BeautifulSoup navigates the HTML tree with `find()` and `find_all()`
- The difference between `.text` and `.get("attribute")`
- Why `response.encoding = "utf-8"` matters for special characters like £

---

### `multipage-scrape.py` — Multi-page scraping + file output
Extended the basic scraper to loop through all 50 pages of the books site. Collects title, price, and stock status for all 1000 books and writes everything to a `.txt` file.

**What I learned:**
- Building URLs dynamically in a loop
- The difference between using a dictionary vs a list for data collection
- Why duplicate keys silently overwrite in a dictionary (discovered via The Star-Touched Queen appearing twice with different prices)
- How to write structured output to a file with proper encoding
- Using `any()` with a generator expression for clean keyword checking

---

### `multipage-scrape_selenium.py` — Selenium + BeautifulSoup
Same multi-page book scraper but powered by Selenium instead of requests. Built this to understand the difference between static and JavaScript-rendered pages.

**What I learned:**
- Why `requests` returns empty content on JS-rendered pages (`data-bind` and framework-rendered content)
- How Selenium controls a real Chrome browser headlessly
- What each Chrome option actually does (`--headless`, `--no-sandbox`, `--disable-gpu`, `--remote-debugging-port`)
- The importance of opening the driver once outside a loop — not 50 times inside it
- How `driver.page_source` gives you the fully rendered HTML

---

### `ai_Parsing.py` — Scraping + Claude AI integration
The main project. A full pipeline that takes a job posting URL, scrapes the page with Selenium, validates the content, sends it to Claude AI, and returns structured JSON with all the job fields automatically extracted.

**The Pipeline:**
```
URL input
    ↓
scrapeJob(url) — Selenium renders page, BeautifulSoup extracts text
    ↓
Keyword validation — confirms it's actually a job posting
    ↓
getFormData(url) — sends text to Claude API
    ↓
Claude extracts: job_name, company_name, location, role_name,
                 work_arrangement, deadline, job_description
    ↓
Structured JSON returned
```

**What I learned:**
- How to write a robust scraping function with `try/except/finally`

- How `soup.get_text()` extracts clean readable text from HTML
- Using `any()` with keyword lists to validate page content
- How to call the Anthropic Claude API from Python
- How to parse Claude's JSON response and strip markdown code fences


---

## Tech Stack

| Tool | Purpose |
|---|---|
| `requests` | Fetching static HTML pages |
| `BeautifulSoup4` | Parsing HTML structure |
| `Selenium` | Rendering JavaScript pages via headless Chrome |
| `webdriver-manager` | Auto-managing ChromeDriver versions |
| `Claude API (Haiku)` | AI-powered field extraction from scraped text |

---

## Install

```bash
pip install requests beautifulsoup4 selenium webdriver-manager anthropic
```

For the AI parsing you'll need an Anthropic API key. Create a `config.py`:

```python
api_key = "your-key-here"
```

And add `config.py` to your `.gitignore`.

---

## Why I Built This

This repo was built as a foundation for a real feature I'm adding to **[InternIn](https://github.com/Mechamorph1903/InternIn)** — my internship tracking app. 

Right now users have to manually fill in every field when adding a job application. With this scraping + AI pipeline, users will just paste the job posting URL and the form fills itself automatically. The knowledge I gained here — especially combining Selenium with Claude — will directly improve the experience for every InternIn user applying for jobs.

There's more to optimize. Speed is the obvious next benchmark/focus — Selenium is slow and every second counts when you're applying to hundreds of jobs. Future improvements include a `requests` fast path for static pages, smarter content extraction before sending to Claude, and eventually a proper job board API integration layer.

But for a first pass, I'm proud of what I learnt in a week.

---

## What's Next

- [ ] Flask endpoint integration into InternIn
- [ ] Rate limiting and retry logic for blocked sites
- [ ] Batch processing for multiple URLs
- [ ] Support for PDF job postings

---

*Built by Daniel Anorue — Computer Science, University of Southern Mississippi*  
*Part of the InternIn project — making job applications less painful*

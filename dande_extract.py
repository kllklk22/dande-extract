# dande
# proxy-aware arxiv extraction. 
# requires local chromedriver.

import sys, random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
]

def extract(query):
    opts = Options()
    for arg in ['--headless', '--disable-gpu', '--no-sandbox']: opts.add_argument(arg)
    opts.add_argument(f'user-agent={random.choice(AGENTS)}')
    
    d = webdriver.Chrome(options=opts)
    try:
        d.get(f"https://arxiv.org/search/?query={query}&searchtype=all")
        d.implicitly_wait(3)
        for r in d.find_elements(By.CSS_SELECTOR, "li.arxiv-result"):
            print(f"{r.find_element(By.CSS_SELECTOR, 'p.title').text.strip()}\n{r.find_element(By.CSS_SELECTOR, 'p.list-title > a').get_attribute('href')}\n---")
    finally:
        d.quit()

if __name__ == "__main__":
    if len(sys.argv) > 1: extract(sys.argv[1])
      

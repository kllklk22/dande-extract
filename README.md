# dande-extract

if you're trying to aggregate open-source academic literature and keep hitting 429 too many requests, use this. 

it's a headless selenium pipeline that rotates user agents and bypasses rigid html structures. it targets arxiv. don't ask me to modify this to scrape paywalled nature articles, i'm not catching a federal cfaa charge for you.

**run:**
`pip install selenium`
`python dande_extract.py "quantum computing"`

# utils/uci_scraper.py

import requests
from bs4 import BeautifulSoup
from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

def search_uci(intent):
    keywords = " ".join(intent.get("keywords", [])).lower().split()
    url = "https://archive.ics.uci.edu/dataset"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")
    datasets = []

    for tag in soup.find_all("a", href=True):
        text = tag.text.strip()
        href = tag['href']
        if not text:
            continue

        # Fuzzy match against each keyword
        if any(similar(text.lower(), kw) > 0.5 for kw in keywords):
            datasets.append({
                "title": text,
                "url": f"https://archive.ics.uci.edu{href}",
                "description": text
            })

    return datasets[:10]

"""Minimal Image search API call — one typed row per image.

Docs & schema: https://quanticdata.io/collectors/image-scraper-api/
"""
import json
import os

import requests

API = "https://api.quanticdata.io/v1/scraper/collectors/search_images/run"
KEY = os.environ["QD_API_KEY"]  # https://quanticdata.io/

payload = {
        "query": "proxy server diagram",
        "country": "us",
        "max_results": 20
    }

r = requests.post(
    API,
    headers={"Authorization": f"Bearer {KEY}", "Content-Type": "application/json"},
    json=payload,
    timeout=180,
)
r.raise_for_status()
data = r.json()["payload"]

for row in data["results"]:
    print(row.get("title"), row.get("thumbnail"), row.get("image"))
print(f"{len(data['results'])} images, cost ${data['cost']}")

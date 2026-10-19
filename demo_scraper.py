"""
Kleinanzeigen.de Immobilien Scraper — Privatverkäufer & €/m² Arbitrage-Detektor — Open-Source Lite Demo
Full real-time DACH data terminal & instant CSV/Excel export (no coding required):
-> https://valora-data-intelligence.web.app/?vertical=immo&utm_source=github&utm_campaign=kleinanzeigen-immobilien-privat-scraper
"""
import json
from scrapling.fetchers import Fetcher

def run_demo():
    print("Loading sample DACH intelligence stream for: immo...")
    print("For full 24/7 enriched feeds (including Impressum CEO, Email & Phone), visit:")
    print("👉 https://valora-data-intelligence.web.app/?vertical=immo&utm_source=github&utm_campaign=kleinanzeigen-immobilien-privat-scraper")
    with open("sample_preview.json", encoding="utf-8") as f:
        sample = json.load(f)
    for idx, row in enumerate(sample, 1):
        print(f"[{idx}] {row.get('title')} | {row.get('seller_name')} | {row.get('price_formatted')}")

if __name__ == "__main__":
    run_demo()

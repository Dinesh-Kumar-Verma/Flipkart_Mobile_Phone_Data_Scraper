import random, time
from scraper.fetcher import get_soup
from scraper.parser import parse_cards
from scraper.pagination import get_next_page
from utils.logger import get_logger

logger = get_logger("pipeline")

def run_pipeline(start_url):
    all_rows = []
    page = 1
    url = start_url

    while url:
        logger.info(f"Processing page {page}")
        
        soup = get_soup(url)
        parsed = parse_cards(soup)

        if len(parsed["Product Name"]) == 0:
            logger.warning("Blank page. Retrying…")
            soup = get_soup(url)
            parsed = parse_cards(soup)

        if len(parsed["Product Name"]) == 0:
            logger.error("No data even after retry. Stopping.")
            break

        rows = list(zip(*parsed.values()))
        all_rows.extend(rows)

        url = get_next_page(soup)
        page += 1
        
        time.sleep(random.uniform(1.5, 3.0))

    return all_rows

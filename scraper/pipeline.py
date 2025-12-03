import random, time
from scraper.fetcher import get_soup
from scraper.parser import parse_cards
from scraper.pagination import get_next_page
import pandas as pd
from utils.cleaners import extract_all_specs
from utils.paths import ensure_dirs
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
        
    df = pd.DataFrame(all_rows, columns=[
        "Product Name", "Price", "Ratings & Reviews", "Star Rating", 
        "Camera", "Memory", "Battery", "Display"
    ])
    
    ensure_dirs(["./data/raw", "./data/processed"])

    
    df.to_csv("./data/raw/raw_flipkart_mobile_data.csv", index=False)
    logger.info("Exported final dataset to raw_flipkart_mobile_data.csv")
    
    clean_df =extract_all_specs(df)
    clean_df.to_csv("./data/processed/clean_flipkart_mobile_data.csv", index=False)
    logger.info("Exported final dataset to data/processed/clean_flipkart_mobile_data.csv")        
        
    return df, clean_df

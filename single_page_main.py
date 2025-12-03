from scraper.fetcher import get_soup
from scraper.parser import parse_cards
import pandas as pd
from utils.logger import get_logger
from utils.cleaners import extract_all_specs
from utils.paths import ensure_dirs


logger = get_logger("singele_page_main")


if __name__ == "__main__":
    
    ensure_dirs(["./data/raw", "./data/processed"])

    url = "https://www.flipkart.com/search?q=mobile+phones"

    soup = get_soup(url)
    raw_data = parse_cards(soup)

    df = pd.DataFrame(raw_data)
    clean_df = extract_all_specs(df)
    
    df.to_csv("./data/raw/raw_single_page_data.csv", index=False)
    logger.info("Exported: raw_single_page_data.csv")
    
    clean_df.to_csv("./data/processed/clean_single_page_data.csv", index=False)
    logger.info("Exported: clean_single_page_data.csv")


    
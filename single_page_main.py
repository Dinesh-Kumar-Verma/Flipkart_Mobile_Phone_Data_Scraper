from scraper.fetcher import get_soup
from scraper.parser import parse_cards
import pandas as pd
from utils.logger import get_logger

logger = get_logger("singele_page_main")


if __name__ == "__main__":
    url = "https://www.flipkart.com/search?q=mobile+phones"

    soup = get_soup(url)
    final_data = parse_cards(soup)

    df = pd.DataFrame(final_data)
    df.to_csv("./data/raw/raw_single_page_data.csv", index=False)
    logger.info("Exported: raw_single_page_data.csv")
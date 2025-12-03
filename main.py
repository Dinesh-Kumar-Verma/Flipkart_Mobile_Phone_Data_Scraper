import pandas as pd
from scraper.pipeline import run_pipeline
from utils.logger import get_logger

logger = get_logger("main")

if __name__ == "__main__":
    url = "https://www.flipkart.com/search?q=mobile+phones"

    logger.info("Starting Flipkart scraping pipeline…")

    run_pipeline(url)

    logger.info("Pipeline completed successfully.")
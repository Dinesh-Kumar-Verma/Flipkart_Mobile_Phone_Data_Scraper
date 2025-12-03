import pandas as pd
from scraper.pipeline import run_pipeline
from utils.logger import get_logger

logger = get_logger("main")

if __name__ == "__main__":
    url = "https://www.flipkart.com/search?q=mobile+phones"

    logger.info("Starting Flipkart scraping pipeline…")

    records = run_pipeline(url)

    df = pd.DataFrame(records, columns=[
        "Product Name", "Price", "Ratings & Reviews", "Star Rating", 
        "Camera", "Memory", "Battery", "Display"
    ])

    df.to_csv("./data/raw/raw_flipkart_mobile_data.csv", index=False)
    logger.info("Exported final dataset to raw_flipkart_mobile_data.csv")

    logger.info("Pipeline completed successfully.")
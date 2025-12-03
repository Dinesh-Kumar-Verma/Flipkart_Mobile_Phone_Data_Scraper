from utils.logger import get_logger
logger = get_logger("pagination")

def get_next_page(soup):
    next_btn = soup.find("a", class_="jgg0SZ", string="Next")

    if next_btn:
        url = "https://www.flipkart.com" + next_btn["href"]
        logger.info(f"Next page found: {url}")
        return url
    
    logger.info("No more pages found.")
    return None

from curl_cffi import requests
import time
import random
from bs4 import BeautifulSoup
from utils.logger import get_logger

logger = get_logger("fetcher")

def get_soup(url):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/128.0.0.0 Safari/537.36"
        )
    }

    session = requests.Session(impersonate="chrome")

    for attempt in range(5):
        try:
            logger.info(f"Request attempt {attempt+1}: {url}")
            resp = session.get(url, headers=headers, timeout=15, impersonate="chrome")

            if resp.status_code == 529:
                wait = random.uniform(3, 7)
                logger.warning(f"Throttled (529) — waiting {wait:.1f}s…")
                time.sleep(wait)
                continue

            resp.raise_for_status()
            logger.info("Page fetched successfully.")
            return BeautifulSoup(resp.text, "html.parser")

        except Exception as err:
            logger.error(f"Fetch error: {err}")
            time.sleep(random.uniform(2, 5))

    raise Exception("Failed after retries.")

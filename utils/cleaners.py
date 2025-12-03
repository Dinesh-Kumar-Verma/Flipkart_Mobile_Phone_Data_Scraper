import re
from utils.logger import get_logger

logger = get_logger("cleaners")

def extract_price(x):
    try:
        value = int(re.sub(r"[^\d]", "", x))
        return value
    except Exception:
        logger.warning(f"Failed to extract price from: {x}")
        return None


def extract_ratings_reviews(x):
    try:
        ratings = int(re.search(r"([\d,]+)\s*Ratings", x).group(1).replace(",", ""))
        reviews = int(re.search(r"([\d,]+)\s*Reviews", x).group(1).replace(",", ""))
        return ratings, reviews
    except Exception:
        logger.warning(f"Failed to extract ratings & reviews from: {x}")
        return None, None


def extract_camera(camera_str):
    try:
        rear = int(re.search(r"(\d+)MP", camera_str).group(1))
        front = int(re.search(r"(\d+)MP Front", camera_str).group(1))
        return rear, front
    except Exception:
        logger.warning(f"Failed to extract camera specs from: {camera_str}")
        return None, None


def extract_memory(memory_str):
    try:
        ram = int(re.search(r"(\d+)\s*GB RAM", memory_str).group(1))
        rom = int(re.search(r"(\d+)\s*GB ROM", memory_str).group(1))

        ext = re.search(r"Expandable Upto\s*(\d+)\s*TB", memory_str)
        expandable = int(ext.group(1)) * 1000 if ext else 0

        return ram, rom, expandable
    except Exception:
        logger.warning(f"Failed to extract memory from: {memory_str}")
        return None, None, None


def extract_battery(battery_str):
    try:
        return float(re.search(r"(\d+)\s*mAh", battery_str).group(1))
    except Exception:
        logger.warning(f"Failed to extract battery from: {battery_str}")
        return None


def extract_display(display_str):
    try:
        cm = float(re.search(r"([\d.]+)\s*cm", display_str).group(1))
        inch = float(re.search(r"([\d.]+)\s*inch", display_str).group(1))
        dtype = display_str.split()[-2]  # e.g., “HD+ Display” → HD+
        return inch, cm, dtype
    except Exception:
        logger.warning(f"Failed to extract display from: {display_str}")
        return None, None, None

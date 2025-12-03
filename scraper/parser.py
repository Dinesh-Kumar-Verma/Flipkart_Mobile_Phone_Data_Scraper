from utils.logger import get_logger

logger = get_logger("parser")

def parse_cards(soup):
    data = {
        "Product Name": [],
        "Price": [],
        "Ratings & Reviews": [],
        "Star Rating": [],
        "Camera": [],
        "Memory": [],
        "Battery": [],
        "Display": []
    }

    cards = soup.find_all("div", class_="ZFwe0M row")
    logger.info(f"Found {len(cards)} product cards.")

    for card in cards:
        name = card.find("div", class_="RG5Slk")
        price = card.find("div", class_="hZ3P6w DeU9vF")
        rating = card.find("div", class_="a7saXW")
        star_rating = card.find("span", class_="CjyrHS")
        specification = card.find("ul", class_="HwRTzP")

        if not name:
            continue

        data["Product Name"].append(name.text.strip())
        data["Price"].append(price.text if price else None)
        data["Ratings & Reviews"].append(rating.text.strip() if rating else None)
        data["Star Rating"].append(star_rating.text.strip() if star_rating else None)
        
        specs = [li.text.strip() for li in specification.find_all("li")] if specification else []

        data["Camera"].append(specs[2] if len(specs) > 2 else None)
        data["Memory"].append(specs[0] if len(specs) > 0 else None)
        data["Battery"].append(specs[3] if len(specs) > 3 else None)
        data["Display"].append(specs[1] if len(specs) > 1 else None)

    return data

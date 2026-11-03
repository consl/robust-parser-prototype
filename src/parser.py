from typing import List, Dict, Any
from bs4 import BeautifulSoup
from .utils import fetch_with_retry
import logging

logger = logging.getLogger(__name__)

def parse_catalog_page(url: str) -> List[Dict[str, Any]]:
    """
    Parses the catalog page and returns a list of items.
    Adapted to the quotes.toscrape.com structure for demonstration.
    """
    try:
        resp = fetch_with_retry(url)
        # lxml is faster and more resilient to broken HTML than html.parser
        soup = BeautifulSoup(resp.text, "lxml")

        items = []
        # Selectors for the demo site (in a real scenario, these would be .product-card, etc.)
        for card in soup.select(".quote"):
            text_el = card.select_one(".text")
            author_el = card.select_one(".author")
            
            if not (text_el and author_el):
                continue

            item = {
                "item_name": author_el.get_text(strip=True),
                "description": text_el.get_text(strip=True),
                "source_url": url,
                "category": "demo_category"
            }
            items.append(item)

        logger.info("Successfully parsed %d items from %s", len(items), url)
        return items

    except Exception as e:
        logger.error("Failed to parse %s: %s", url, e, exc_info=True)
        raise
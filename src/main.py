import os
import json
import logging
from pathlib import Path
from .parser import parse_catalog_page

# Настраиваем логирование: уровень, формат, вывод в stdout (для Docker)
logging.basicConfig(
    level=os.getenv("LOG_LEVEL", "INFO").upper(),
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s"
)

def main() -> None:
    url = os.getenv("TARGET_URL", "https://quotes.toscrape.com")
    output_path = os.getenv("OUTPUT_PATH", "/data/output.json")

    logger = logging.getLogger(__name__)
    logger.info("Starting parser for: %s", url)

    items = parse_catalog_page(url)

    # Гарантируем создание директории, если её нет
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(items, f, ensure_ascii=False, indent=2)
        
    logger.info("Saved %d items to %s", len(items), output_path)

if __name__ == "__main__":
    main()
from config import BASE_URL, START_PAGE, END_PAGE
from utils.logger import setup_logger
from utils.session_manager import create_session
from core.fetcher import Fetcher
from core.extractor import Extractor
from services.product_service import ProductService
from exporters.csv_exporter import export_csv

logger = setup_logger()
session = create_session()

fetcher = Fetcher(session, logger)
extractor = Extractor()
service = ProductService(fetcher, logger)

all_rows = []

for page in range(START_PAGE, END_PAGE + 1):

    listing_url = f"{BASE_URL}/page/{page}/"

    soup = fetcher.fetch(listing_url)

    if not soup:
        continue

    links = extractor.get_product_links(soup)

    for link in links:

        rows = service.scrape_product(link)

        all_rows.extend(rows)

export_csv(all_rows)

print("SCRAPING COMPLETED")
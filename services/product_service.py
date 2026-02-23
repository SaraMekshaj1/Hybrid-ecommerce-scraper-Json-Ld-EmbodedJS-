from parsers.jsonld_parser import parse_json_ld
from parsers.variation_parser import parse_variants
from core.normalizer import combine_product_variants

class ProductService:

    def __init__(self, fetcher, logger):
        self.fetcher = fetcher
        self.logger = logger

    def scrape_product(self, url):

        soup = self.fetcher.fetch(url)

        if not soup:
            return []

        product = parse_json_ld(soup)

        # 🚨 skip bad product pages
        if not product:
            self.logger.warning(f"No JSON-LD found: {url}")
            return []

        form = soup.find("form", class_="variations_form")

        variants = []

        if form:
            variants = parse_variants(form)

        return combine_product_variants(product, variants)
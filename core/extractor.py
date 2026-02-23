class Extractor:

    def get_product_links(self, soup):

        links = []
        products = soup.select("li.product a.woocommerce-LoopProduct-link")

        for p in products:
            links.append(p.get("href"))

        return links
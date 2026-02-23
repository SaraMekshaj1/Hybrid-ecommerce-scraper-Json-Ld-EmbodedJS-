from bs4 import BeautifulSoup

class Fetcher:

    def __init__(self, session, logger):
        self.session = session
        self.logger = logger

    def fetch(self, url):
        try:
            self.logger.info(f"Fetching: {url}")

            r = self.session.get(url)
            r.raise_for_status()

            self.logger.info(f"Success: {url}")

            return BeautifulSoup(r.text, "lxml")

        except Exception as e:
            self.logger.error(f"Fetch failed: {url} - {e}")
            return None
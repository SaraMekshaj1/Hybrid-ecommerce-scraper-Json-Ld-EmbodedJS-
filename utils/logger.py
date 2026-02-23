import logging

def setup_logger():

    logger = logging.getLogger("scraper")
    logger.setLevel(logging.INFO)

    if not logger.handlers:

        file_handler = logging.FileHandler("scraper.log", encoding="utf-8")
        formatter = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s"
        )

        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    return logger
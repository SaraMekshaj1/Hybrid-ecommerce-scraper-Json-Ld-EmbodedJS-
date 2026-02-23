import json

def parse_json_ld(soup):
    scripts = soup.find_all("script", type="application/ld+json")

    for script in scripts:
        try:
            data = json.loads(script.string)

            if isinstance(data, list):
                for item in data:
                    if item.get("@type") == "Product":
                        return normalize_product(item)

            if isinstance(data, dict):

                if "@graph" in data:
                    for item in data["@graph"]:
                        if item.get("@type") == "Product":
                            return normalize_product(item)

                if data.get("@type") == "Product":
                    return normalize_product(data)
        except:
            continue

    return {}

def normalize_product(item):

    offer = item.get("offers", [{}])[0]

    return {
        "name": item.get("name"),
        "sku": item.get("sku"),
        "description": item.get("description"),
        "image": item.get("image"),
        "currency": offer.get("priceCurrency"),
        "url": item.get("url")
    }
import csv

def export_csv(data, filename="products_variants.csv"):

    if not data:
        return

    keys = [
    "name",
    "sku",
    "description",
    "image",
    "currency",
    "url",
    "variant_sku",
    "price",
    "stock",
    "in_stock",
    "size",
    "color",
    "variant_image"
]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)
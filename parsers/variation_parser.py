import json
def find_attr(attrs, keyword):

    if isinstance(attrs, dict):

        for k, v in attrs.items():
            if keyword in k:
                return v

    if isinstance(attrs, list):

        for a in attrs:
            name = a.get("name", "")
            if keyword in name:
                return a.get("option")

    return None

def clean_attr(value):

    if not value:
        return None

    return str(value).replace("-", " ").title()

def parse_variants(form):

    variants = []

    data = form.get("data-product_variations")

    if not data:
        return []

    variations = json.loads(data)

    for v in variations:

        attrs = v.get("attributes", {})

        size = find_attr(attrs, "size")
        color = find_attr(attrs, "color")

        variants.append({
            "variant_sku": v.get("sku"),
            "price": v.get("display_price"),
            "stock": v.get("max_qty") or (1 if v.get("is_in_stock") else 0),
            "in_stock": v.get("is_in_stock"),
            "size": clean_attr(size),
            "color": clean_attr(color),
            "variant_image": v.get("image", {}).get("src")
        })

    return variants
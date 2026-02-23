def combine_product_variants(product, variants):

    rows = []

    if not variants:

        rows.append({
            **product,
            "variant_sku": product.get("sku"),
            "price": None,
            "stock": None,
            "in_stock": None,
            "size": None,
            "color": None,
            "variant_image": product.get("image")
        })

        return rows

    for v in variants:
        row = {
            **product,
            **v
        }
        rows.append(row)
        
    return rows
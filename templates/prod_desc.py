def product_desc_template(product: dict, logic_blocks: dict) -> dict:
    return {
        "product_name": product["name"],
        "ingredients": product["ingredients"],
        "benefits": logic_blocks["benefits_text"],
        "usage": logic_blocks["usage_text"],
        "price": product["price"]
    }

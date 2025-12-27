def product_desc_template(product: dict, logic_blocks: dict) -> dict:
    return {
        "product_name": product["name"],
        "ingredients": product["ingredients"],
        "benefits": logic_blocks["generate_benefits"],
        "usage": logic_blocks["extract_usage"],
        "price": product["price"]
    }

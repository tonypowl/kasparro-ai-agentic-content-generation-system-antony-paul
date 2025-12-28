#sample product in dataset vs random product X 
from logic_blocks.compare_prices_block import compare_prices

def comparison_template(product_a: dict, product_b: dict) -> dict:
    return {
        "product_a": product_a,
        "product_b": product_b,
        "price_difference": compare_prices(product_a["price"], product_b["price"])
    }

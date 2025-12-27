import json
from templates.faq import faq_template
from templates.prod_desc import product_desc_template
from templates.comparision import comparison_template

class PageFormatAgent:
    def run(self, product: dict, content: dict):
        faq = faq_template(content["questions"], content["logic_blocks"])
        product_page = product_desc_template(product, content["logic_blocks"])

        product_b = {
            "name": "Antony Face Wash",
            "ingredients": ["Salicylic Acid"],
            "benefits": ["Anti Acne"],
            "price": 799
        }   
        comparison = comparison_template(product, product_b)

        with open("outputs/faq.json", "w") as f:
            json.dump(faq,f,indent=2)

        with open("outputs/product_page.json", "w") as f:
            json.dump(product_page,f,indent=2)

        with open("outputs/comparison_page.json", "w") as f:
            json.dump(comparison,f,indent=2)
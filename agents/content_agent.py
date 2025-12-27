from logic_blocks.generate_benefits_block import generate_benefits
from logic_blocks.extract_usage_block import extract_usage
from logic_blocks.compare_prices_block import compare_prices

class ContentAgent:
    def run(self, product:dict)->dict:
        #to generate questions and reusable blocks
        questions = {
            "informational":[
                "What is the  name of the product?",
                "What are the main ingredients?",
                "What are the suitable skin types?",
                "What are the benefits using it?"
            ],
            "safety":[
                "Are there any side effecs?",
                "Is it safe for sensitive skin?"
            ],
            "usage":[
                "How should be it be applied?",
                "When should it be applied?",
                "How much should be applied?"
            ],
            "purchase":[
                "How much does it cost?"
            ]
        }

        logic_blocks = {
            "benefits_text": generate_benefits(product["benefits"]),
            "usage_text": extract_usage(product["usage"]),
            # "comparision_text": compare_prices()
        }

        return {
            "questions": questions,
            "logic_blocks": logic_blocks
        }

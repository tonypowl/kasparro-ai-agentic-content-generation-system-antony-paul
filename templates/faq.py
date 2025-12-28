#minumum 5 q's 
def faq_template(questions: dict, logic_blocks: dict) -> dict:
    faq_items = []

    for category, qs in questions.items():
        for question in qs:
            faq_items.append({
                "category": category,
                "question": question,
                "answer": select_answer(category, logic_blocks)
            })

    return {"faq": faq_items}

def select_answer(category: str, logic_blocks: dict) -> str:
    if category == "usage":
        return logic_blocks["usage_text"]
    elif category == "informational":
        return logic_blocks["benefits_text"]
    elif category == "purchase":
        return "Refer to product price for more details."
    elif category == "safety":
        return "Please follow usage instructions carefully."
    return ""

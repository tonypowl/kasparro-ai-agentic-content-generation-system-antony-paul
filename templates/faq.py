#minumum 5 q's 
def faq_template(questions: dict, logic_blocks: dict) -> dict:
    faq_items = []
    for category, qs in questions.items():
        for q in qs:
            faq_items.append({
                "question": q,
                "answer": logic_blocks.get("generate_benefits")
            })
            
    return {"faq": faq_items}

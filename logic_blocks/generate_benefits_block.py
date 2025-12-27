def generate_benefits(benefits: list[str]) -> str:
    if not benefits:
        return ""
    return "Helps with " + " and ".join(benefits)

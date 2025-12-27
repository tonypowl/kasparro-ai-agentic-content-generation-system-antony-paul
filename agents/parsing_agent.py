class ParsingAgent:
    def run(self, data: dict) -> dict:
        #to convert raw data into a more normalized version without unecessary chars
        return {
            "name": data.get("Product Name"),
            "concentration": data.get("Concentration"),
            "skin_type": [s.strip() for s in data.get("Skin Type", "").split(",")],
            "ingredients": [i.strip() for i in data.get("Key Ingredients", "").split(",")],
            "benefits": [b.strip() for b in data.get("Benefits", "").split(",")],
            "usage": data.get("How to Use"),
            "side_effects": data.get("Side Effects"),
            "price": int(data.get("Price").replace("₹", ""))
        }
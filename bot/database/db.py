import uuid
import json

class Product:
    JSON_FILE = "bot/database/products.json"

    def save_product(self, product_data: dict) -> None:
        with open(self.JSON_FILE) as f:
            data = json.loads(f.read())

            data.append(product_data)
        
        with open(self.JSON_FILE, 'w') as f:
            f.write(json.dumps(data, indent=4))

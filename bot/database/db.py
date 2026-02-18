import json


class Product:
    JSON_FILE = "bot/database/products.json"

    def save_product(self, product_data: dict) -> None:
        with open(self.JSON_FILE, encoding="utf-8") as f:
            data = json.loads(f.read())

            max_id = max((item["id"] for item in data), default=0)

            product_data["id"] = max_id + 1

            data.append(product_data)

        with open(self.JSON_FILE, "w", encoding="utf-8") as f:
            f.write(json.dumps(data, indent=4))

    def products_list(self) -> list[dict[str : str | int]]:
        with open(self.JSON_FILE, encoding="utf-8") as f:
            products = json.loads(f.read())

            return products


product = Product()

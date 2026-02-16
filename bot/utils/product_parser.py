REQUIRED_FIELDS = {"name", "price", "description"}
OPTIONAL_FIELDS = {"brand", "memory", "color", "discount"}

class Utils:
    def parse_product_caption(self, text: str) -> dict:
        result = {}

        for line in text.split("\n"):
            if ":" not in line:
                continue

            key, value = line.split(":", 1)
            key = key.strip().lower()
            value = value.strip()

            if key in REQUIRED_FIELDS or key in OPTIONAL_FIELDS:
                result[key] = value

        return result

    def validate_product_data(self, data: dict):
        missing = REQUIRED_FIELDS - data.keys()
        if missing:
            return False, f"Majburiy field yetishmayapti: {', '.join(missing)}"

        try:
            data["price"] = int(data["price"])
        except ValueError:
            return False, "price son bo‘lishi kerak"

        if "discount" in data:
            data["discount"] = int(data["discount"])

        return True, None

utils = Utils()
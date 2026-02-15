from bot.database.db import Product

class ProductService:

    def __init__(self):
        self.product = Product()
    

    def create_product(self, data: dict):
        return self.product.save_product(data)
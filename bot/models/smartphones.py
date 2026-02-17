from bot.database.db import product

class Smartphone:
    def __init__(self, name, price, description, brand, memory, color, discount, photo, id):
        self.name = name
        self.price = price
        self.description = description
        self.brand = brand
        self.memory = memory
        self.color = color
        self.discount = discount
        self.photo = photo
        self.id = id
    
    def discounted_price(self):
        percent = self.price / 100
        d = self.discount * percent
        return self.discount - d

    
data_list = product.products_list()
smartphones = [Smartphone(**item) for item in data_list]
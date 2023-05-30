import random

class Stock:
    def __init__(self, stock_id, price):
        self.stock_id = stock_id
        self.price = price

    def generate_price(self):
        self.price += random.uniform(-1, 1)


    #def __str__(self):
    #    return f"Stock {self.stock_id} with price {self.price}"
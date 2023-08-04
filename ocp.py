class Products:
    def __init__(self,price):
        self.price = price

    def get_price(self):
        return self.price

class discounted_price(Products):
    def __init__(self,price,discount):
        super().__init__(price)
        self.discount = discount

    def get_price(self):
        return self.price - (self.price * self.discount)

def calculated_price(products):
    total_price = 0
    for product in products:
        total_price += product.get_price()
    return total_price

# Using the calculate_total_price function with a list of products
products = [Products(100), discounted_price(50, 0.1), Products(75)]
print("Total Price:", calculated_price(products))

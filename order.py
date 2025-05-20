from customer import Customer
from coffee import Coffee

class Order:
    all = []
    def __init__(self, customer,coffee, price):
        if isinstance(customer, Customer):
            self.customer = customer
            customer._orders.append(self)

        if isinstance(coffee, Coffee):
            self.coffee = coffee
            coffee._orders.append(self)

        Order.all.append(self)
        self.price = price

    @property
    def price(self):
        return self._price 
    
    @price.setter
    def price(self, value):
        if not isinstance(value, float):
            raise ValueError("Price must be a float")
        if not (1.0 <= value <= 10.0):
            raise ValueError("Price must be between 1.0 and 10.0.")
        self._price = value
    
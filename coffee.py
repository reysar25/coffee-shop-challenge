class Coffee:
    def __init__(self,name):
        self.name = name 
        self._orders = []
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Coffe name must be a string.")
        
        if not (3 <= len(value)):
            raise ValueError("Name must be atleast 3 characters.")
        
        self._name = value 

    def orders(self):
        from order import Order
        orders = [order for order in Order.all if order.coffee == self]
        return orders
    
    def customers(self):
        from order import Order
        return list(set(order.customer for order in Order.all if order.coffee == self))
    
    def num_orders(self):
        if self._orders:
            return len(self._orders)
        
        return 0
    
    def average_price(self):
        from order import Order
        coffee_orders = [order for order in Order.all if order.coffee == self]
        if not coffee_orders:
            return 0
        return sum(order.price for order in coffee_orders)/len(coffee_orders)
from debug import Order
from coffee import Coffee

class Customer:
    def __init__(self,name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if not isinstance(value,str):
            raise TypeError("Name must be a string")
        if not 1 <= len(value) <= 15:
            raise ValueError("Name must be between 1 and 15 charactes ")
        self._name = value

    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        return list({order.coffee for order in self.orders()})
    
    def make_order(self,coffee,price):
        return Order(self,coffee,price)
    
    @classmethod
    def most_order(cls,coffee):
        if not isinstance(coffee,Coffee):
            raise TypeError('Must be a coffee')
        
        customers = {}
        for order in Order.all:
            if order.coffee == coffee:
                if order.customer in customers:
                    customers[order.customer] += order.price

        if not customers:
            return None
        return max(customers.items(), key=lambda item: item[1])
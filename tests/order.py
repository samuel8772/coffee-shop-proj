from customer import Customer
from coffee import Coffee

class Order:
    all = []

    def __init__(self,customer,coffee,price):
        self.customer = customer
        self.price = price
        self.coffee = coffee
        Order.all.append(self)

    @property
    def customer(self):
        return self._customer
    
    @customer.setter
    def customer(self,value):
        if not isinstance(value,Customer):
            raise TypeError("Must be a customer")
        self._customer = value

    @property  
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self,value):
        if not isinstance(value,Coffee):
            raise TypeError("Must be a coffee") 
        self._coffee = value   

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self,value):
        if not isinstance(value,float):
            raise TypeError("Price must be a float")
        if not 1.0 <= value <= 10.0:
            raise ValueError("Price must be between 1.0 and 10.0")
        if hasattr(self,"_price"):
            raise AttributeError("price cannot be changed")
        self._price = value
        
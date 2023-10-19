class Coffee:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>2 and not hasattr(self, "name"):
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if self == order.coffee]
    
    def customers(self):
        unique_customers = []
        for order in Order.all:
            if order.coffee == self and order.customer not in unique_customers:
                unique_customers.append(order.customer)
        return unique_customers
    
    def num_orders(self):
        count = 0
        for order in Order.all:
            if order.coffee == self:
                count += 1
        return count
    
    def average_price(self):
        total_prices = [order.price for order in Order.all if order.coffee == self]
        sum_prices = sum(total_prices)
        num_prices = len(total_prices)
        return sum_prices/num_prices

class Customer:
    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name)>0 and len(name)<16:
            self._name = name
        
    def orders(self):
        return [order for order in Order.all if order.customer == self]
    
    def coffees(self):
        unique_coffees = []
        for order in Order.all:
            if order.customer == self and order.coffee not in unique_coffees:
                unique_coffees.append(order.coffee)
        return unique_coffees
    
    def create_order(self, coffee, price):
        if isinstance(coffee, Coffee):
            return Order(self, coffee, price)
    
class Order:
    all = []

    def __init__(self, customer, coffee, price):
        self.customer = customer
        self.coffee = coffee
        self.price = price
        Order.all.append(self)

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        if isinstance(price, float) and price >= 1.0 and price <= 10.0 and not hasattr(self, "price"):
            self._price = price

    @property
    def customer(self):
        return self._customer

    @customer.setter
    def customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer

    @property
    def coffee(self):
        return self._coffee

    @coffee.setter
    def coffee(self, coffee):
        if isinstance(coffee, Coffee):
            self._coffee = coffee
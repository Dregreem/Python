import csv

class Item:

    all = []
    pay_rate = 0.8  # Discounted price

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0):
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"

        self.__name = name
        #self._name = name
        #makes it read only add one _ but still could be accessed 
        #by the instance 
        #it you use two __ then it becomes a private and can not
        #be accesed by an instance
        self.price = price
        self.quantity = quantity

        Item.all.append(self)

    def calculate_total_price(self):
        return self.price * self.quantity

    def apply_discount(self):
        self.price = self.price * self.pay_rate

    def __repr__(self):
        return f"{self.__class__.__name__} : '{self.name}', {self.price}, {self.quantity})"
        #self.__class__.__name__ tells the type of the object 

    @classmethod
    def instantiate_from_csv(cls):
        with open('item.csv', 'r') as f:
            reader = csv.DictReader(f)
            items = list(reader)

        for item in items:
            Item(
                name=item.get('name'),
                price=float(item.get('price')),
                quantity=int(item.get('quantity'))
            )

    @staticmethod
    def is_integer(num):
        # We will count out the floats that are point zero
        if isinstance(num,float):
            return num.is_integer() #return false
        elif isinstance(num,int):
            return True
        else:
            return False

    @property
    def name(self):
        #creates a fixed property
        #Property Decorator= Read-Only Attribute
        return self.__name
        #the name of the variable is still name this is a
        #pythonic way
    """@name.setter
    def name(self,value):
        #allows it to be changed 
        #a varible is required if we want to change it
        #could be used to fixate the name or to control the 
        actions that will happen after it is setted
        self.__name=value
    """



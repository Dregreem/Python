import csv

class Item:

    all = []
    pay_rate = 0.8  # Discounted price

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0):
        assert price > 0, f"Price {price} is not greater than zero"
        assert quantity > 0, f"Quantity {quantity} is not greater than zero"

        self.name = name
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

class Phone(Item):

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0, broken_phones: int=0):
        # Call the super function to have access to all the attributes/methods
        super().__init__(
            name,price,quantity
        )
        assert broken_phones>=0,f" Broken Phones {broken_phones}can not be negative"

        
        self.broken_phones=broken_phones


phone1=Phone("İphone11",500,5,1)

print(Item.all)
print(Phone.all)



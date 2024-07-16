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
        return f"Item('{self.name}', {self.price}, {self.quantity})"

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

print(Item.is_integer(7.5))


#Static Method:




# Assuming 'item.csv' is in the correct path and has the appropriate headers
#Item.instantiate_from_csv()

# Print all instantiated items
#print(Item.all)

#Yes, exactly. By using a class method, we can perform operations that involve the class itself, 
# such as instantiating multiple objects and modifying class-level data. In your example, 
# the instantiate_from_csv method reads from a CSV file and creates instances of the Item class 
# (or its subclasses) based on the data in the file. These instances are then added to the class-level list Item.all.
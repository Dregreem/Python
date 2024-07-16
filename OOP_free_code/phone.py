import csv
from item import Item

class Phone(Item):

    def __init__(self, name: str = "", price: float = 0, quantity: int = 0, broken_phones: int=0):
        # Call the super function to have access to all the attributes/methods
        super().__init__(
            name,price,quantity
        )
        assert broken_phones>=0,f" Broken Phones {broken_phones}can not be negative"

        
        self.broken_phones=broken_phones
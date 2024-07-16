class Item:
    all=[]
    pay_rate=0.8 #Discounted price

    def __init__(self,name: str=" ",price: float =0,quantity: int=0):

        assert price>0,f"Price {price} is not greater than zero"
        assert quantity>0,f"Quantity {quantity} is not greater than zero"

        self.name=name
        self.price=price
        self.quantity=quantity
        
        #Actions to Execute
        Item.all.append(self)
        #adds the created object to the list
        
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
            self.price=self.price*self.pay_rate

    def __repr__(self):
         #to control the output when the list is written
         return f"Item('{self.name}',{self.price},{self.quantity})"
    

item1=Item("Phone",100,1)
item2=Item("Laptop",1000,3)
item3=Item("Cable",10,5)
item4=Item("Mouse",50,5)
item5=Item("Keyboard",75,5)

print(Item.all)

#for object in Item.all:
 #    print(f"{object.name} is {object.price} and we have {object.quantity}")
     
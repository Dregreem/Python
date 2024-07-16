class Item:
    pay_rate=0.8 #Discounted price

    def __init__(self,name: str=" ",price: float =0,quantity: int=0):

        #Run validations to the received arguments
        assert price>0,f"Price {price} is not greater than zero"
        assert quantity>0,f"Quantity {quantity} is not greater than zero"

        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
        
    def calculate_total_price(self):
        return self.price*self.quantity
    
    def apply_discount(self):
            self.price=self.price*self.pay_rate
            #Now it will take the values for the objects

        #self.price=self.price*Item.pay_rate
        #can not be accesed through the item it must be through the class
        #this way it will always take the class attribute not the object 

item1=Item("Phone",100,5)
item1.apply_discount()
print(item1.price)

item2=Item("Laptop",1000,5)
item2.pay_rate=0.7
item2.apply_discount()
print(item2.price)



#Class attributes could be accesed by items and the class level

#print(Item.pay_rate)
#print(item1.pay_rate)

#print(Item.__dict__) #all attributes for Class Level
#print(item1.__dict__)  #all attributes for Instance Level

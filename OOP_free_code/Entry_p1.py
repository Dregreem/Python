class Item:
    #constructer:__init__

    def __init__(self,name:str=0,price:float =0,quantity:int=0):

        #Run validations to the received arguments
        assert price>0,f"Price {price} is not greater than zero"
        assert quantity>0,f"Quantity {quantity} is not greater than zero"

        #Assign to self object
        self.name=name
        self.price=price
        self.quantity=quantity
        

    def calculate_total_price(self):
        return self.price*self.quantity

item1=Item("Phone",100,5)
item2=Item("Laptop",1000,3)

print (f"The total price of {item1.name} is {item1.calculate_total_price()}")
print (f"The total price of {item2.name} is {item2.calculate_total_price()}")





#self,name:str=0,price:int =0,quantity:int=0  Litterally wtf python 

""""
random_str="aaaa"
print(random_str.upper())

"""
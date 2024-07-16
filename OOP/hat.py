import random

class Hat:
    @classmethod
    def sort(cls,name):
        print(name,"is in ","the house ",random.choice(cls.houses))
    
    #def __init__(self):
        #self.houses=["Dragon","Tiger","Bear","Turtle"]

    houses=["Dragon","Tiger","Bear","Turtle"]
        

#hat=Hat()
#with classmethod we dont need to create a object we can access it with Hat but
#still the object could use it this is a easy way to decrease the number of the objects
Hat.sort("Harry")


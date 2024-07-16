#When to use class and when to use static method

class Item:
    @staticmethod
    def is_integer(num):
        """
        This should do something that has a relationship to the class but 
        not something unique per instance!
        """
    @classmethod
    def instantate_from_something(cls):
        """
        This should also do something that has a relationship with 
        the class,but usually thosre are used to manipuşate 
        different structures of data to instantiate objects,like 
        we have done with CSV
        """
    #Called with the class 
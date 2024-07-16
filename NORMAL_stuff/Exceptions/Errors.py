#Syntax Errors are for us to solve
#Run time Errors are for the values are entered by the user
#Name Error is an error that a variable is not defined or not exist 
""""When cat is entered
try:
    x=int(input("What is the value of X? "))
except ValueError:
    print("X is not an integer")


print(f"x is {x}")
"""

def main():
    x=get_int("What is the value of X? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
            #This way it would be easy to handle the text change
            x=int(input(prompt))
        except ValueError:
            #print("X is not an integer")
            pass
            #another mechanism for handling we just skip it the userr wont learn if something is wrong
        else:
            #if there is no error or any of the errors are not defined 
            break
    return x

"""" Shortest way
def ge_int2():
    while True:
        try:
            return int(input("what is x?"))
        except ValueError:
            print("X is not an integer")
"""
main()






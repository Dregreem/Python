def main():
    Num=int(input("Please enter a Number: "))
    if parity2(Num):
        print("the number is Even")
    else:
        print("The number is Odd")

#Normal Human Beings
def parity(Num):
    if Num%2==0:
        return True
    else:
        return False
    
#A little bit effected by Python
def parity2(Num):
    return True if Num%2==0 else False

#The shortest version_you are the Python
def parity3(Num):
    return Num%2==0

main()


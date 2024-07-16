"""
names=[]

for __ in range(3):
    names.append(input("What is your name? "))

for name in sorted(names):
    print(f"Hello, {name}")
"""

"""
# w means write but it always rewriting it 
# a for append but it adds them as a text not as a line

file=open("names.txt","a")
#writes to the file
file.write(f"{name}\n")

#saves the file
file.close()
"""

"""write to a file method2
name=input("What is your name? ")
with open("names.txt","a") as file:
    file.write(f"{name}\n")
    #in this format the file is directly closed
"""
"""Read data from file
with open("names.txt","r") as file:
    for line in file:
    # Erases the empty lines
        print("Hello",line.rstrip())
"""

"""Writing out the names
with open("names.txt") as file:
    for line in sorted(file):
        print("hello,",line.rstrip())

with open("names.txt") as file:
    for line in sorted(file, reverse=True):
        print("hello,",line.rstrip())
"""


"""Version-1
#With while loop
i = 0
while i < 10:
    print("Meow")
    i += 1
"""
"""Version-2
# []this is a list the code will act accoridng the number of the specimens
for i in[]:
    print("Meow")
"""
"""Version-3
for _ in range(3):
    print("meow")
"""
"""#the most Pythonic way
print("meow\n"*3,end="")
#End is required for the final line 
"""
"""Version-4
while True:
    n=int(input("What is n? "))
    if n>0:
        break

for _ in range(n):
    print("meow")
"""
"""With Functions
def main():
    meow(get_value())

def meow(n):
    for _ in range(n):
        print("Meow")

def get_value():
    while True:
        n=int(input("What is n? "))
        if n>0:
            break 
    return n  
    
main()
"""

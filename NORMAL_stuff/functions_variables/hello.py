name=input("What is your Name ").strip().title()
print("Hello "+ name)
"""
#another way from the basics of the print function
print("Hello",end="??? ")
print(name)

# a weird way to automaticly assign str?
print(f"hello,{name}")

#Astetics and Grammar

#remove white space but only in the front of the name
name=name.strip()
#Capitilize the first letter of the string
name=name.capitalize()
#Capitilize all the first letters
name=name.title()

#to chain the functions
name=name.strip().title()

"""

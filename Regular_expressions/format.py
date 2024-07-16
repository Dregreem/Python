import re

name = input("What is your name? :").strip()

"""
if ", "in name:
    last,first=name.split(", ")
    name=(f"{first} {last}")

print(f"Hello, {name}")
"""
# Check if the name contains a comma

#:= valrus operator could be used ro ask and assign 

if matches := re.search(r"^(.+), *(.+)$", name):
    # Extract the first and last names
    last = matches.group(1)
    first = matches.group(2)
    # Reformat the name
    name = f"{first} {last}"

print(f"Hello, {name}")

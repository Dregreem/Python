email=input("What is your Email? ").strip()
"""
if "@"in email and "." in email:
    print("Valid")
else:
    print("Invalid")
"""

username,domain=email.split("@")

if (username) and domain.endswith(".edu"):
    print("Valid")
else:
    print("Invalid")
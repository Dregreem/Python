import csv
"""Normal Way
name=input("What is your name?")
home=input("where do you live")

with open("students_made.csv","a")as file:
    writer=csv.writer(file)
    writer.writerow([name,home])
"""

name=input("What is your name?")
home=input("where do you live")

with open("students_made.csv","a")as file:
    writer=csv.DictWriter(file,fieldnames=["name","home"])
    writer.writerow({"name":name,"home":home})
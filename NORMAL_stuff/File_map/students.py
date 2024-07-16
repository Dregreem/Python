"""#read CSV and interpret the data
with open("students.csv")as file:
    for line in file:
        row=line.rstrip().split(",")
        print(f"{row[0]} is in {row[1]}")
# same code but more readable 
with open("students.csv")as file:
    for line in file:
        name,house=line.rstrip().split(",")
        print(f"{name} is in {house}")
"""
""" Without CSV lİB
students=[]
with open("students.csv") as file:
    for line in file:
        name,house,home=line.rstrip().split(",")
        student={"name":name,"house":house,"home":home}
        students.append(student)

# Print student details
#Sorting students according to the a certain order
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']}also lives in {student['home']}")

# A nameless function which only called once -> key=lambda student: student["name"]
"""

"""CSV reader as a text reader
import csv
students=[]

with open("students.csv") as file:
    reader=csv.reader(file)
    for row in reader:
        students.append({"name":row[0],"house":row[1],"home":row[2]})
  

# Print student details
#Sorting students according to the a certain order
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']} also lives in {student['home']}")
"""

import csv
students=[]

with open("students.csv") as file:
    reader=csv.DictReader(file)
    #changed the csv file add the titles of the sections
    #because this is a dictionary reader therefore we have to pinpoint the data
    # The advantage of the Dİctionary is that as the csv file changes(added new columns) the code wont be affected by it 
    for row in reader:
        students.append({"name":row["name"],"house":row["house"],"home":row["home"]})
  

# Print student details
#Sorting students according to the a certain order
for student in sorted(students, key=lambda student: student["name"], reverse=True):
    print(f"{student['name']} is in {student['house']} also lives in {student['home']}")
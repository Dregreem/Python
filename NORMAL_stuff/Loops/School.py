Students=["Kerem","Furkan","Anil","Kader"]
Houses=["A","B","C","D"]

"""VERSION-1
for students in Students:
    print(students)
"""
"""VERSION-2
for i in range(len(Students)):
    print(i+1, Students[i])
"""

#Dictionary
students={
    "Kerem":"A",
    "Furkan":"B",
    "Anil":"C",
    "Kader":"D"
          }

#print(students["Kerem"])
for student in students:
    print(student,"->", students[student])

"""VERSION-3
for student in students:
    #The outuput will be the keys
    print(student)
"""



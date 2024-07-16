students=[
    {"name":"Kerem","house":"A","patronus":"Dragon"},
    {"name":"Furkan","house":"B","patronus":None},
    {"name":"Anil","house":"C","patronus":"Parrot"},
    {"name":"Kader","house":"D","patronus":"Tardis"},
    #None can be used in python 
]
for student in students:
    print(student["name"], student["house"],student["patronus"], sep=",")
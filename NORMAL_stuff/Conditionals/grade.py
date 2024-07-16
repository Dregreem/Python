score=int(input("What is your score: "))

if score>=90 and score <=100:
    print("Grade A")
elif 80<=score <90:
    #python is allowing it to be used this way
    print("Grade B")
elif score>=70 and score <=80:
    print("Grade C")
elif score>=60 and score <=70:
    print("Grade D")
else:
    print("Grade F")

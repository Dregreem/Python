def main2():
    student=Student()
    #student[1]="Dragon"
    # a tupple objects value cant be changed 
    # a list and dictionaries could be changed but a tuple can not 
    print(f"{student.name} from {student.house}")

class Student:
    def __init__(self):
        self.name = self.get_name()
        self.house =self.get_house()
        self.potronus=self.get_potronus()

    def get_name(self):
        name = input("Name: ")
        if not name:
            raise ValueError("Name cannot be empty")
        return name

    def get_house(self):
        house = input("House: ")
        if house not in ["Dragon", "Tiger", "Lion"]:
            raise ValueError("Invalid House")
        return house
    
    def __str__(self):
        return f"{self.name} is a studen from {self.house}"
    
    def get_potronus(self):
        potronus = input("Potronus: ")
        if not potronus:
            raise ValueError("Potronus cannot be empty")
        return potronus
    def charm(self):
        #self does not mean that the function will be se used when it is initiated
        print("BOOOOOOO")
    

def main():
    try:
        student = Student()
        print(student)
        student.charm()
        #print(f"{student.name} from {student.house}")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


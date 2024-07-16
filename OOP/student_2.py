class Student:
    def __init__(self):
        self.name = self.get_name()
        self._house = self.get_house()

    def get_name(self):
        name = input("Name: ")
        if not name:
            raise ValueError("Name cannot be empty")
        return name
    
    def get_house(self):
        house = input("House: ")
        if not house:
            raise ValueError("House cannot be empty")
        return house

    @property
    def house(self):
        return self._house

    @house.setter
    def house(self, house):
        if house not in ["Dragon", "Tiger", "Lion"]:
            raise ValueError("Invalid House")
        self._house = house

    def __str__(self):
        house = self.house if self.house else "Unknown House"  # Handle None case
        return f"{self.name} is a student from {house}"

def main():
    try:
        student = Student()
        print(student)
        #student.house = "Kerem" 
         # This will raise a ValueError because "Kerem" is not a valid house
         #using a setter avoid it to be changed cant be overried but only the newly assigned value not in the terminal 
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()

name = input("What is your name? : ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("bOO")
    case "Drago":
        print("Abra")
    case _:
        print("Who?")
        # for the default cases

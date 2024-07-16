def main():
    print_rectangle(3,4)

def print_column(height):
    for _ in range(height):
        print(("#"))

def print_row(width):
    print("?"*width)

def print_rectangle(height,width):
    for i in range(height):
           print("_"*width)

main()
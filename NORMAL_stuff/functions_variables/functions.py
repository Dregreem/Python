def main():
    name=input("what is your name? ")
    hello(name)


def hello(to="World"):
    print("Hello ",to)
    #We have assigned a initial value as World if no input would
    #comes to the function it will print out Hello World

main()

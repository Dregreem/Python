def main():
    height=int(input("Height: "))
    pyramid(height)

def pyramid(n):
    for i in range(n):
        print("#"*(i+1))

main()
#breakpoints: only analyze the code that the coder had limited

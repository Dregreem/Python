#sys.argv takes the all the words by words that are entered by the user 
import sys

try:
    print("Hello, my name is", sys.argv[1])
except IndexError:
    print("Too few arguments")


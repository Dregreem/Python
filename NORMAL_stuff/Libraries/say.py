import cowsay
import sys

if len(sys.argv) == 2:
    cowsay.tux("hello")
else:
    print("Usage: python say.py <name>")

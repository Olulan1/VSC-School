import sys
try:
    x = int(input())
    y = int(input())
    print(x*y)
except ValueError:
    sys.exit("That is not a number.")
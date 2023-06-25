import sys

try:
    x=int(input("x:"))
    y=int(input("y:"))
    
except ValueError:
    print("Error! Values must be in numerical system.")
    sys.exit(1)
    
try:
    res=x/y
    
except ZeroDivisionError:
    print("Error! The value of y cannot be zero.")
    sys.exit(1)
    
print(f"The result is {res}")
    
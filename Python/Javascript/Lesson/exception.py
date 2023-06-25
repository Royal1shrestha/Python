try:
    numerator = int(input("Enter the numerator : "))
    denominator = int(input("Enter the denominator : "))
    result = numerator/denominator
    print(result)
    
except ZeroDivisionError:
    print("Error!Denominator can't be zero.")
    
except ValueError:
    print("Error!Enter an integer value.")
    
except Exception:
    print("Error!")
    
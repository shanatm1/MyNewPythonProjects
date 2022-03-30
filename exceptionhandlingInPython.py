#Exception is events detected during the execution of the program that interrupt the
#execution of the program

try:
    numerator = int(input("enter a number to devide: "))
    denominator = int(input("Enter a number to devided by: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("u cant devide by zero!")
except ValueError:
    print(" use only numbers to devide")
except Exception:
    print("something went wrong")
else:
    print(result)
finally:
    print("this will execute evrything :)")
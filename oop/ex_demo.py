
try:
    num = int(input("Enter a number :"))
    print( 100 / num)
except ZeroDivisionError:
    print("Please provide a non-zero")
except ValueError:
    print("Invalid input. Please enter a valid number!")

print("The End")





x = int(input("Please enter the value of x = "))
operator = (input("Please enter the operator = "))
y = int(input("Please enter the value of y = "))

if operator == "+":
    print(f"The sum of x and y is {x + y}")

elif operator == "-":
    print(f"The subtraction of x and y is {x - y}")

elif operator == "*":
    print(f"The multiplication of x and y is {x * y}")

elif operator == "/":
    if y != 0:
        print(f"The division of x and y is {x / y}")
    else:
        print("Error! Division by zero is not possible.")

else:
    print("Error! Unknown Operator.")

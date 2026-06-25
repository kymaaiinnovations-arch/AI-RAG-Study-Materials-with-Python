number_one = float(input("Enter the first number: "))
number_two = float(input("Enter the second number: "))    

operation = input("Enter the operation (+, -, *, /): ") 
if operation == "+":
    result = number_one + number_two
    print("The result is:", result)
elif operation == "-":
    result = number_one - number_two
    print("The result is:", result)
elif operation == "*":
    result = number_one * number_two
    print("The result is:", result)
elif operation == "/":
    if number_two != 0:
        result = number_one / number_two
        print("The result is:", result)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Invalid operation. Please enter one of +, -, *, or /.")


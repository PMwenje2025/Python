# Simple Calculator Program

# Define the numbers
num1 = float(input("Enter first number (e.g., 23): "))
num2 = float(input("Enter second number (e.g., 17): "))
opr  = input("Enter operation (+, -, *, /): ")

# Perform the calculation
if opr == "+":
    result = num1 + num2
elif opr == '-':
    result = num1 - num2
elif opr == '*':
    result = num1 * num2
elif opr == '/':
    if num2 != 0:
        result = num1 / num2
    else:
        result = "Error: Division by zero"
else:
    result = "Error: Invalid operation"

# Final result
print("Result:", result)

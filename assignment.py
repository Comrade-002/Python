# Simple Calculator Program

# Function to perform calculation based on the operator
def calculate(num1, num2, operator):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    else:
        return "Invalid operator"

# Main program
print("Simple Calculator")
print("Operations: +, -, *, /")

try:
    # Get user input
    num1 = float(input("Enter the first number: "))
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform calculation and display result
    result = calculate(num1, num2, operator)
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is undefined.")

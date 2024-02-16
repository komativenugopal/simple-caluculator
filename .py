def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Cannot divide by zero."

# Get user input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Get user choice
choice = input("Enter choice (1/2/3/4): ")

# Perform calculation based on user choice
if choice in ('1', '2', '3', '4'):
    if choice == '1':
        result = add(num1, num2)
        operation = 'Addition'
    elif choice == '2':
        result = subtract(num1, num2)
        operation = 'Subtraction'
    elif choice == '3':
        result = multiply(num1, num2)
        operation = 'Multiplication'
    elif choice == '4':
        result = divide(num1, num2)
        operation = 'Division'

    print(f"{operation} result: {result}")
else:
    print("Invalid choice. Please enter 1, 2, 3, or 4.")

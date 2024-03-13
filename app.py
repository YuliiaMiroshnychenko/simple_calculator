def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def divide(num1, num2):
    if num2 == 0:
        return "Error: Cannot divide by zero!"
    else:
        return num1 / num2

def multiply (num1, num2):
    return num1 * num2

if __name__ == "__main__":
    print("Welcome to Simple Calculator CLI App")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter 'add' to add, 'sub' to subtract or 'div' to divide, or 'mul' to multiply: ")

    if operation.lower() == "add":
        print("Result:", add(num1, num2))
    elif operation.lower() == "sub":
        print("Result:", subtract(num1, num2))
    elif operation.lower() == "div":
        print("Result:", divide(num1, num2))
    elif operation.lower() == "mul":
        print("Result:", multiply(num1, num2))
    else:
        print("Invalid operation entered. Please enter 'add', 'sub' or 'div' or 'mul'.")

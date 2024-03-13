def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

if __name__ == "__main__":
    print("Welcome to Simple Calculator CLI App")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter 'add' to add, 'sub' to subtract: ")

    if operation.lower() == "add":
        print("Result:", add(num1, num2))
    elif operation.lower() == "sub":
        print("Result:", subtract(num1, num2))
    else:
        print("Invalid operation entered. Please enter 'add', 'sub'.")

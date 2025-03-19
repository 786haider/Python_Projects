print("\n Simple calculator program \n")
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error! Division by zero is not allowed."
    return x / y

def main():
    print("Operations:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    
    while True:
        # Get operation choice from user
        choice = input("\nEnter operation number (1-4) or 'q' to quit: ")
        
        # Check if user wants to exit
        if choice.lower() == 'q':
            print("Calculator closing. Goodbye!")
            break
            
        # Check if input is valid
        if choice not in ['1', '2', '3', '4']:
            print("Invalid input! Please enter a number between 1 and 4.")
            continue
            
        # Get input numbers
        try:
            num1 = int(input("Enter first number: "))
            num2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
            
        # Perform calculation based on operation choice
        if choice == '1':
            print(f"The sum of {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"The difference of {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"The product of {num1} * {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            result = divide(num1, num2)
            print(f"The quotient of {num1} / {num2} = {result}")

if __name__ == "__main__":
    main()
def print_ones_digit(num):
    """
    Prints the ones digit of the given number.
    
    Args:
        num (int): The number whose ones digit we want to print
    """
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    number = int(input("Enter a number: "))
    print_ones_digit(number)

if __name__ == "__main__":
    main()
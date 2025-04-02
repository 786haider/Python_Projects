def user_number():
    return int(input('Enter a number: '))
def main():
    for i in range(user_number()):
        if is_odd(i):
            print('odd')
        else:
            print('even')
            
def is_odd(value: int):
    """
    Checks to see if a value is odd. If it is, returns true.
    """
    
    remainder = value % 2  # 0 if value is divisible by 2, 1 if it isn't
    return remainder == 1



if __name__ == '__main__':
    main()
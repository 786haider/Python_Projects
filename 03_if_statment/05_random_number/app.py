
import random

N_NUMBERS : int = 10
MIN_VALUE : int = 1
MAX_VALUE : int = 100

def main():
    value : list[int] = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print(value)

if __name__ == '__main__':
    main() 
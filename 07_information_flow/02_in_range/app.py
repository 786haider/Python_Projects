def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high

def main():
    print(in_range(1,3, 5))
    print(in_range(5,3, 1))
if __name__ == "__main__":
    main()
    

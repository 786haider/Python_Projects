inches_in_feet : int = 12
def main():
    feet: float = float(input("Enter the number of feet: "))
    inches: float = feet * inches_in_feet
    print(feet, "feet is equal to", inches, "inches")
if __name__ == "__main__":
    main()
import math
def main():
    AB = float(input("Enter the length of side AB: "))
    AC = float(input("Enter the length of side AC: "))
    BC = math.sqrt(AB**2 + AC**2)
    print(f"The length of BC (the hypotenuse) is " + str(BC))
if __name__ == "__main__":
    main()
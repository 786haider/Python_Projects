def main():
    print("Hello World! To find the perimeter of triangle fill the requirments")
    side_1 = float(input("What is the length of side A? "))
    side_2 = float(input("What is the length of side B? "))
    side_3 = float(input("What is the length of side C? "))
    perimeter = (side_1 + side_2 + side_3)
    print(f"The perimeter of your triangle is {perimeter}")
    
    
if __name__ == "__main__":
    main()
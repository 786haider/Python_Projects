def main():
    print("Hello World ! This is the data of Anton, Beth, Chen, Drew, Ethan ages.")
    anton__age : int = 21
    beth_age = anton__age + 6
    chen_age = beth_age + 20
    drew_age = chen_age + anton__age
    ethan_age = chen_age
    print(f"Anton is {anton__age} years old.")
    print(f"Beth is {beth_age} years old.")
    print(f"Chen is {chen_age} years old.")
    print(f"Drew is {drew_age} years old.")
    print(f"Ethan is {ethan_age} years old.")
    print(f"The sum of their ages is {anton__age+beth_age+chen_age+drew_age+ethan_age}.")
    print(f"The average age is {(anton__age+beth_age+chen_age+drew_age+ethan_age)/5}")
    print(f"The difference between the oldest and youngest is {max(anton__age,beth_age,chen_age,drew_age,ethan_age)-min(anton__age,beth_age,chen_age,drew_age,ethan_age)}")
if __name__ == "__main__":
    main()
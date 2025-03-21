
C : int =299792458 #speed of light in m/s
def main():
    user_given_mass: float =float(input("Enter mass in kg :"))
    energy_in_juoles: float=user_given_mass * (C**2)
    print("e = m * C^2...")
    print("m = " + str(user_given_mass) + " kg")
    print("C = " + str(C) + " m/s")
    print(str(energy_in_juoles) + " joules of energy!")
if __name__ == "__main__":
    main()




 
def main():
    print("Hello World ! Welcome to your temperature converter")
    degrees_fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
    degrees_celsius = (degrees_fahrenheit - 32) * 5.0/9.0
    print(f"{degrees_fahrenheit} degrees fahrenheit equals {degrees_celsius:.2f} degrees celsius")
if __name__ == "__main__":
 main()
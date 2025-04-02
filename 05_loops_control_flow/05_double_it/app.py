def main():
    # Ask user for a starting number
    user_input = input("Enter a number: ")
    
    # Convert input to a number
    curr_value = float(user_input)
    
    # Store the original value to show in results
    original_value = curr_value
    
    # Create a list to store all values
    results = [curr_value]
    
    # Double the value until it reaches or exceeds 100
    while curr_value < 100:
        curr_value = curr_value * 2
        results.append(curr_value)
    
    # Print the results
    print(f"Starting with {original_value}, doubling until reaching ≥ 100:")
    print(" ".join(str(int(value)) if value.is_integer() else str(value) for value in results))


# This provided line is required at the end of
# Python file to call the main() function.
if __name__ == '__main__':
    main()
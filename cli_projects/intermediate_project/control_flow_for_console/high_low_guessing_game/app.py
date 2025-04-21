import random

def main():
    NUM_ROUNDS = 5
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    score = 0
    for round_num in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_num}")
        
        computer_number = random.randint(1, 100)
        player_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        valid_guess = False
        while not valid_guess:
            guess = input("Do you think your number is higher or lower than the computer's?: ").lower()
            if guess in ["higher", "lower"]:
                valid_guess = True
            else:
                print("Please enter either higher or lower: ", end="")
    
        if player_number > computer_number and guess == "higher":
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif player_number < computer_number and guess == "lower":
            print(f"You were right! The computer's number was {computer_number}")
            score += 1
        elif player_number == computer_number:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        else:
            print(f"Aww, that's incorrect. The computer's number was {computer_number}")
        
        print(f"Your score is now {score}")
 
        if round_num < NUM_ROUNDS:
            print()
    
    if score == NUM_ROUNDS:
        print("\nWow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("\nGood job, you played really well!")
    else:
        print("\nBetter luck next time!")
    
    print("Thanks for playing!")

if __name__ == "__main__":
    main()
# =============================================================================
# Description    : Classic Number Guessing Game with 3 difficulty levels
#                  Guess the secret number and win a crown!
#                  Easy   → 1–10
#                  Medium → 1–50
#                  Hard   → 1–250
# Usage          : Run → python3 number_guess.py
#                  Choose level, then start guessing! Enter 0 anytime to quit.
# =============================================================================

import random                  # For generating the secret number

# Let user choose difficulty level
level = int(input("Enter level\n1 Easy\n2 Medium\n3 Hard\n> "))

# Set the range based on selected level
if level == 1:
    num = random.randint(1, 10)       # Easy: 1 to 10
elif level == 2:
    num = random.randint(1, 50)       # Medium: 1 to 50
elif level == 3:
    num = random.randint(1, 250)      # Hard: 1 to 250
else:
    print("Invalid choice")
    num = None                        # Prevent further play on invalid input

# Only start the game if a valid level was chosen
if num is not None:
    print("\nGame started! Try to guess the secret number.\n")
    
    choice = 1                        # Controls the main game loop
    while choice:                     # Loop until user chooses to quit
        guess = int(input("Enter your Guess : "))
        
        if guess == num:
            print("YOU WON")
            break                     # Exit loop on correct guess
        elif guess < num:
            print("NO You Guessed Smaller than target")
        else:  # guess > num
            print("NO You Guessed Larger than target")
        
        # Ask if user wants to try again or quit
        choice = int(input("Enter 0 to quit, 1 to retry: "))
    
    print("\nTHANK YOU & BYE", end='')

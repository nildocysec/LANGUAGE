# =============================================================================
# Description    : Rock Paper Scissors Game against the computer
#                  Use: rock, paper, or scissor (or emojis!)
#                  First to win? Just play for fun!
# Usage          : Run → python3 rock_paper_scissor.py
#                  Type your choice and press Enter. Play as long as you want!
# =============================================================================

import random

# Valid choices (normalized to lowercase)
valid_choices = ["rock", "paper", "scissor"]

# Mapping for nicer display with emojis
emoji_map = {
    "rock": "Rock",
    "paper": "Paper",
    "scissor": "Scissor"
}

print("Rock Paper Scissors Game")
print("Enter your move (or type 'quit' to exit)\n")

while True:
    # Get and normalize user input
    user_input = input("Enter Rock, Paper, Scissor : ").strip().lower()

    # Allow quitting gracefully
    if user_input in ["quit", "exit", "q"]:
        print("\nThanks for playing! See you next time!")
        break

    # Map common variations and emojis
    if user_input.startswith("r"):
        U_choose = "rock"
    elif user_input.startswith("p"):
        U_choose = "paper"
    elif user_input.startswith("s"):
        U_choose = "scissor"
    else:
        U_choose = user_input  # rely on exact match below

    # Computer makes a random choice
    I_choose = random.choice(valid_choices)

    # Show both choices with nice formatting
    user_display = emoji_map.get(U_choose, U_choose.title())
    comp_display = emoji_map.get(I_choose, I_choose.title())
    
    print(f"\nYou chose → {user_display}")
    print(f"I chose   → {comp_display}\n")

    # Check for draw
    if U_choose == I_choose:
        print("Draw – Great minds think alike!")

    # Winning combinations for user
    elif (U_choose, I_choose) in [("rock", "scissor"),
                                  ("scissor", "paper"),
                                  ("paper", "rock")]:
        print("YOU WIN! You're a champion!")

    # Losing combinations
    elif (I_choose, U_choose) in [("rock", "scissor"),
                                  ("scissor", "paper"),
                                  ("paper", "rock")]:
        print("You Lose – I win this time!")

    # Invalid input
    else:
        print("Invalid choice! Please enter: rock, paper, or scissor")
        print("   (You can also use just 'r', 'p', 's' or emojis!)\n")
        continue  # Skip to next round without breaking

    print("-" * 40)  # Separator for clean rounds

print("\nEND", end='')
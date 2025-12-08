# =============================================================================
# Description    : Multi-Dice Roller – Roll any number of dice at once!
#                  Shows each die result + total sum
#                  Perfect for board games, D&D, or just fun!
# Usage          : Run → python3 roll_dice.py
#                  Enter how many dice → then type 'y' to roll, 'n' to quit
# =============================================================================

import random

# Ask user how many dice they want to roll at once
num = int(input("Enter number of dice to roll : "))

# Safety check (prevent too many dice)
if num <= 0:
    print("Please enter a number greater than 0.")
    exit()
elif num > 100:
    print("Whoa! That's a lot of dice... but okay!")

print(f"\nReady to roll {num} dice! Type 'y' to roll, 'n' to quit.\n")

total_rolls = 0   # Keeps track of total dice rolled across all turns

while True:
    ask = input("Roll the dice? (y/n): ").strip().lower()

    if ask == "n" or ask == "no":
        print("\nGame over!")
        break

    elif ask == "y" or ask == "yes" or ask == "":
        print("\nRolling the dice...\n")

        current_sum = 0   # Sum of current roll

        # Roll each die one by one
        for i in range(num):
            die_result = random.randint(1, 6)
            print(f"Die {i+1}: {die_result}")
            current_sum += die_result
            total_rolls += 1

        # Show total for this roll
        print(f"\nTotal for this roll → {current_sum}")
        print("—" * 30)

    else:
        print("Invalid input! Please type 'y' or 'n'")

# Final goodbye message
print(f"\nYou rolled a total of {total_rolls} dice!")
print("THANK YOU & BYE", end='')
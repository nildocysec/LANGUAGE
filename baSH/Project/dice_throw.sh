#!/bin/bash
# =============================================================================
# Description    : Throws any number of dice.
#                  If any die shows 6 → you win and it shows your User ID!
# Usage          : Just run → bash dice_throw.sh
# =============================================================================

echo "Welcome to Lucky Dice Game"
echo "If you roll a 6 → Your secret User ID will be revealed!"
echo "==================================================="

# Ask how many dice the user wants to throw
read -p "Enter number of dice to use : " num

# Safety: make sure user entered a number
if ! [[ "$num" =~ ^[0-9]+$ ]] || [[ $num -lt 1 ]]; then
    echo "Please enter a valid number (1 or more)."
    exit 1
fi

# This variable controls whether to play again
try_again=1

# Main game loop – keeps running until user enters 0
until [[ $try_again -eq 0 ]]
do
    echo ""
    echo "Rolling $num dice..."
    echo "===================="

    i=1
    got_six=0   # will become 1 if any die shows 6

    # Throw each die one by one
    while [[ $i -le $num ]]
    do
        die_out=$(( RANDOM % 6 + 1 ))        # number between 1 and 6
        echo "Die $i → $die_out"

        # If we get a 6 → jackpot!
        if [[ $die_out -eq 6 ]]
        then
            got_six=1
        fi

        ((i++))
    done

    # After all dice – check if we won
    if [[ $got_six -eq 1 ]]
    then
        echo "------------------------"
        echo "JACKPOT! You rolled a 6!"
        echo "Unlocked User ID : $UID"
        echo "------------------------"
    else
        echo "No 6 this time... Better luck next roll!"
    fi

    # Ask if user wants to play again
    echo ""
    read -p "Press 0 to quit, or any key to roll again : " try_again

    # If user types nothing and just presses Enter → continue
    [[ -z "$try_again" ]] && try_again=1
done

echo ""
echo "Thanks for playing! Bye bye!"
echo "=================================="

exit 0
# This program is rock paper scissor game

import random

while True:

    U_choose = input("Enter ✊ Rock, ✋ Paper, ✌️ Scissor : ").lower()
    
    I_choose = random.choice(["rock", "paper", "scissor"])

    print("I chose : ",I_choose)

    if U_choose == I_choose:
        print("🤝 Draw")
 
    elif (U_choose, I_choose) in [("rock", "scissor"),
                              ("scissor", "paper"),
                              ("paper", "rock")]:
        print("🏆 You Win")

    elif (I_choose, U_choose) in [("rock", "scissor"),
                              ("scissor", "paper"),
                              ("paper", "rock")]:
        print("😞 You Lose 💔")

    else:
        print("Invalid choice")
        break


print("END",end='')
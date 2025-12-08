# This program rolls dice

import random

num = int(input("Enter number of dice to roll : "))
counter = 0

while True:

    ask  = input(" Roll dice ? (y/n) 🎲: ").lower()   #convert input to lower case
    if(ask == "n"):
        break

    elif(ask == 'y'):

        die = 0
        dice = 0

        for i in range(num):
            die = random.randint(1,6)
            print("die",i+1,":",die)

            counter = counter +1
            dice = die + dice

        print("dice : ",dice)

    else:
        print("Invalid choice")

print("THANK YOU & BYE",end='')
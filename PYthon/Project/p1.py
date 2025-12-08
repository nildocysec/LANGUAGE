# This program generates a number and user win crown if guessed correct

import random

level = int(input("Enter level\n1 Easy\n2 Medium\n3 Hard\n"))

if(level == 1):
    num = random.randint(1,10)
elif(level == 2):
    num = random.randint(1,50)
elif(level == 3):
    num = random.randint(1,250)
else:
    print("Invalid choice")    

choice = 1
while choice:

    choice = int(input("Enter your Guess : "))
    if(choice == num):
        print(" 🎯 YOU WON 👑 ")
    elif(choice < num):
        print("NO 👎 You Guessed Smaller than target")
    elif(choice > num):
        print("NO 👎 You Guessed Larger than target")
    
    choice = int(input("Enter 0 to quit 1 to retry"))
    if(choice == 0):
        break


print("THANK YOU & BYE",end='')
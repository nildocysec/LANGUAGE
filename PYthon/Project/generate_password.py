# This Program generate random password

import random
import string

char1 = (string.ascii_letters)
char2 = (string.digits)
char3 = (string.punctuation)

char123 = ( char1 + char2 + char3 )

length = int(input("Enter password length you want : "))
password = ""
count = 0
while count < length:
    next_char = random.choice(char123)
    password = password + next_char
    count += 1
print("password : ",password)

print("END",end='')
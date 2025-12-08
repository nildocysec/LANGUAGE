# =============================================================================
# Description    : Generates a strong random password of user-specified length
#                  using letters (upper & lower), digits, and special characters.
# Usage          : Run the script → python3 generate_password.py
#                  Enter desired password length when prompted.
# =============================================================================

import random                  # For generating random characters
import string                  # Provides ready-made character sets

# Define character pools
char1 = string.ascii_letters   # A-Z, a-z (52 characters)
char2 = string.digits          # 0-9 (10 characters)
char3 = string.punctuation     # All special characters like !@#$%^&* etc.

# Combine all allowed characters into one big pool
char123 = char1 + char2 + char3

# Ask user for desired password length
length = int(input("Enter password length you want : "))

# Initialize empty password string and counter
password = ""
count = 0

# Generate password one character at a time
while count < length:
    next_char = random.choice(char123)   # Pick a random character from the pool
    password = password + next_char       # Append it to the password
    count += 1                            # Increment counter

# Display the generated password
print("password : ", password)

# Simple indication that program has finished
print("END", end='')
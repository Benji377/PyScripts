"""
Title: Password Generator
Description: Generates a random sequence of characters
Author: Benji377
Created: 04.07.2023
Last Updated: 04.07.2023

Usage:
    No parameters

Dependencies:
    None

Notes:
    - This script is standalone and does not require other files from the repo.
    - Adjust any parameters or constants at the top of the script as needed.
"""


import random
import string

def generate_password(length=8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Usage example:
# Generates a random password of length 12
password = generate_password(12)
print(password)

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

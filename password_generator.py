
import random
import string

print("Welcome to Random Password Generator")

length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation

password = ""

for i in range(length):
    password += random.choice(characters)

print("Your generated password is:", password)

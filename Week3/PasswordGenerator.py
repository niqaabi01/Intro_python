# list all uppercase letters.....choose 1 randomly
# list all lowercase letters.....choose 1 randomly
# list all special characters.....choose 1 randomly
# list all numbers.....choose 1 randomly

import random

# random.choice(listname)


def passwordgenerator():
    lowercase = ["a", "b", "c", "d", "e", "f"]
    upppercase = ["G", "H", "I", "J", "K", "L"]
    numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    special_chars = ["!", "@", "#", "$", "%", "&"]

    password = random.choice(lowercase) + random.choice(upppercase) + random.choice(numbers) + random.choice(
        special_chars)
    password = password + password
    return password



print("Your password : ", passwordgenerator())
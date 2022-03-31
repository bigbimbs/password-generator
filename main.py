import string
import random

# characters to generate password from

# Stores all lowerCase and upperCase alpha characters
alphabets = list(string.ascii_letters)
# Stores all digits characters
digits = list(string.digits)
# Stores special characters
special_characters = list("!@#$%^&*()_+-={}|[]:;<>?,.")
# Stores all character
characters = list(string.ascii_letters + string.digits + "!@#$%^&*()_+-={}|[]:;<>?,.")


def generate_random_password():
    # Length of password from the user
    length = int(input("Enter the length of password you want to generate   "))
    # number of character types
    alpha_counts = int(input("Enter the number of Alphabets you want in the password    "))
    digit_counts = int(input("Enter the number of Digits you want in the password   "))
    special_characters_counts = int(input("Enter the number of Special Characters you want in the password  "))
    # sum alpha, digits and special_characters count
    characters_count = alpha_counts + digit_counts + special_characters_counts
    # check the total length with characters sum
    # print not valid if the sum is greater than length
    if characters_count > length:
        print("Characters total length is greater than password length specified")
        return

    # initializing the password
    password = []

    # picking random alphabets
    for i in range(alpha_counts):
        password.append(random.choice(alphabets))

    # picking random digits
    for i in range(digit_counts):
        password.append(random.choice(digits))

    for i in range(special_characters_counts):
        password.append(random.choice(special_characters))

    # if the total characters count is less than the password length
    # add random characters to make it equal to the length
    if characters_count < length:
        random.shuffle(characters)
        for i in range(length - characters_count):
            password.append(random.choice(characters))

    # Shuffling the resultant password
    random.shuffle(password)
    # converting the list to string
    # printing the list
    print("".join(password))


generate_random_password()
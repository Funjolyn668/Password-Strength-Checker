
import string
import math
import getpass


def calculate_entropy(password):
    pool_size = 0

    if any(char.islower() for char in password):
        pool_size += 26
    if any(char.isupper() for char in password):
        pool_size += 26
    if any(char.isdigit() for char in password):
        pool_size += 10
    if any(char in string.punctuation for char in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


def get_password_input():
    print("\nPassword Visibility:")
    print("1. Hide password")
    print("2. Show password")

    choice = input("Choose an option (1-2): ").strip()

    if choice == "2":
        return input("Enter password to check: ")

    return getpass.getpass("Enter password to check: ")

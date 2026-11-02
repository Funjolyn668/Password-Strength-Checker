
import string
import secrets
import math
import getpass


# Common passwords
COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "123456789",
    "qwerty123",
    "admin123",
    "iloveyou",
    "welcome123",
    "abc123",
    "letmein"
}


# Password entropy calculator
def calculate_entropy(password):

    pool_size = 0

    if any(c.islower() for c in password):
        pool_size += 26

    if any(c.isupper() for c in password):
        pool_size += 26

    if any(c.isdigit() for c in password):
        pool_size += 10

    if any(c in string.punctuation for c in password):
        pool_size += len(string.punctuation)

    if pool_size == 0:
        return 0

    return len(password) * math.log2(pool_size)


# Password strength checker
def check_password(password):

    score = 0
    suggestions = []

    # Password length
    if len(password) >= 12:
        score += 1
    else:
        suggestions.append("Use at least 12 characters.")

    # Uppercase letters
    if any(c.isupper() for c in password):
        score += 1
    else:
        suggestions.append("Add uppercase letters.")

    # Lowercase letters
    if any(c.islower() for c in password):
        score += 1
    else:
        suggestions.append("Add lowercase letters.")

    # Numbers
    if any(c.isdigit() for c in password):
        score += 1
    else:
        suggestions.append("Add numbers.")

    # Special characters
    if any(c in string.punctuation for c in password):
        score += 1
    else:
        suggestions.append("Add special characters.")

    # Common password detection
    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid commonly used passwords.")
        strength = "WEAK"

    else:
        if score <= 2:
            strength = "WEAK"
        elif score <= 4:
            strength = "MEDIUM"
        else:
            strength = "STRONG"

    # Entropy calculation
    entropy = calculate_entropy(password)

    # Display results
    print("\n========== PASSWORD ANALYSIS ==========")

    print("Password Strength:", strength)
    print("Criteria Passed:", score, "/ 5")
    print(f"Estimated Entropy: {entropy:.2f} bits")

    if suggestions:
        print("\nSecurity Suggestions:")

        for suggestion in suggestions:
            print("-", suggestion)

    else:
        print("\nGood! All five basic criteria are satisfied.")

    print("=======================================")


# Password generator
def generate_password(length=16):

    if length < 12:
        raise ValueError("Password length must be at least 12.")

    lowercase = secrets.choice(string.ascii_lowercase)
    uppercase = secrets.choice(string.ascii_uppercase)
    digit = secrets.choice(string.digits)
    special = secrets.choice(string.punctuation)

    all_characters = (
        string.ascii_letters
        + string.digits
        + string.punctuation
    )

    password = [lowercase, uppercase, digit, special]

    for _ in range(length - 4):
        password.append(secrets.choice(all_characters))

    # Shuffle password characters
    secrets.SystemRandom().shuffle(password)

    return "".join(password)


# Show or hide password input
def get_password_input():

    print("\nPassword Visibility:")
    print("1. Hide password")
    print("2. Show password")

    visibility = input("Choose an option (1-2): ").strip()

    if visibility == "2":

        password = input("Enter password to check: ")

    else:

        password = getpass.getpass("Enter password to check: ")

    return password


# Main program
def main():

    while True:

        print("\n===== PASSWORD STRENGTH CHECKER =====")

        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        # Check password
        if choice == "1":

            password = get_password_input()

            if not password:
                print("Password cannot be empty.")
                continue

            check_password(password)

        # Generate password
        elif choice == "2":

            try:

                length = int(
                    input("Enter password length (minimum 12): ")
                )

                password = generate_password(length)

                print("\nGenerated Password:", password)
                print("Keep this password somewhere secure.")

            except ValueError as error:

                print("Error:", error)

        # Exit program
        elif choice == "3":

            print("\nThank you for using Password Strength Checker!")
            break

        else:

            print("\nInvalid choice. Please enter 1, 2, or 3.")


# Run program
if __name__ == "__main__":
    main()

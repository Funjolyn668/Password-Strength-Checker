
from modules.password_checker import check_password
from modules.password_generator import generate_password
from modules.password_security import get_password_input


def main():
    while True:
        print("\n===== PASSWORD STRENGTH CHECKER =====")
        print("1. Check Password Strength")
        print("2. Generate Strong Password")
        print("3. Exit")

        choice = input("\nEnter your choice (1-3): ").strip()

        if choice == "1":
            password = get_password_input()

            if not password:
                print("Password cannot be empty.")
                continue

            check_password(password)

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

        elif choice == "3":
            print("\nThank you for using Password Strength Checker!")
            break

        else:
            print("\nInvalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    main()


import string

from modules.common_passwords import COMMON_PASSWORDS
from modules.password_security import calculate_entropy


def check_password(password):
    checks = [
        (len(password) >= 12, "Use at least 12 characters."),
        (any(c.isupper() for c in password), "Add uppercase letters."),
        (any(c.islower() for c in password), "Add lowercase letters."),
        (any(c.isdigit() for c in password), "Add numbers."),
        (
            any(c in string.punctuation for c in password),
            "Add special characters."
        )
    ]

    score = sum(passed for passed, _ in checks)

    suggestions = [
        suggestion
        for passed, suggestion in checks
        if not passed
    ]

    if password.lower() in COMMON_PASSWORDS:
        strength = "WEAK"
        suggestions.append("Avoid commonly used passwords.")
    elif score <= 2:
        strength = "WEAK"
    elif score <= 4:
        strength = "MEDIUM"
    else:
        strength = "STRONG"

    entropy = calculate_entropy(password)

    print("\n========== PASSWORD ANALYSIS ==========")
    print(f"Password Strength: {strength}")
    print(f"Criteria Passed: {score}/5")
    print(f"Estimated Entropy: {entropy:.2f} bits")

    if suggestions:
        print("\nSecurity Suggestions:")
        for suggestion in suggestions:
            print(f"- {suggestion}")
    else:
        print("\nGood! All five basic criteria are satisfied.")

    print("=======================================")

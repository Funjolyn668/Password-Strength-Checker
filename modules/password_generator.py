
import string
import secrets


def generate_password(length=16):
    if length < 12:
        raise ValueError("Password length must be at least 12.")

    characters = (
        string.ascii_lowercase
        + string.ascii_uppercase
        + string.digits
        + string.punctuation
    )

    password = [
        secrets.choice(string.ascii_lowercase),
        secrets.choice(string.ascii_uppercase),
        secrets.choice(string.digits),
        secrets.choice(string.punctuation)
    ]

    password.extend(
        secrets.choice(characters)
        for _ in range(length - 4)
    )

    secrets.SystemRandom().shuffle(password)

    return "".join(password)

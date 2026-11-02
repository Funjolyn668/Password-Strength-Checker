🔐 Password Strength Checker

A beginner-friendly Python cybersecurity project that checks password strength, generates secure random passwords, detects commonly used passwords, and estimates password entropy.

📌 Project Overview

The Password Strength Checker is a Python-based application designed to help users understand basic password security.

The program evaluates passwords based on five security criteria and provides suggestions to improve password strength.

It also includes additional features such as a password generator, common password detection, password entropy calculation, and a Show/Hide Password option.

✨ Features
1. Password Strength Checker
Checks whether a password contains at least 12 characters.
Detects uppercase letters (A-Z).
Detects lowercase letters (a-z).
Checks for numerical digits (0-9).
Detects special characters such as @, #, $, and !.
Classifies passwords as WEAK, MEDIUM, or STRONG.
Provides security suggestions to improve password strength.
2. Show/Hide Password Option
Allows users to choose whether their password is visible while typing.
Hide Password uses Python's getpass module.
Show Password uses Python's input function.
Gives users more control over password visibility.
3. Password Generator
Generates random passwords using Python's secrets module.
Allows users to select their preferred password length.
Requires a minimum password length of 12 characters.
Includes uppercase and lowercase letters.
Includes numbers and special characters.
Guarantees at least one character from each required category.
4. Common Password Detection
Checks passwords against a predefined list of commonly used passwords.
Identifies easily guessed passwords.
Automatically classifies detected common passwords as WEAK.
Provides recommendations to avoid commonly used passwords.
5. Password Entropy Calculator
Estimates password randomness in bits.
Calculates entropy based on password length and character pool size.
Helps users understand password complexity.
Uses a mathematical formula to estimate entropy.
6. Additional Features
Interactive menu system.
Continuous password checking without restarting the program.
Input validation.
Error handling for invalid password generator lengths.
Exit option to close the application.
📊 Password Strength Criteria

The application evaluates passwords using five basic security requirements.

Criteria	Requirement
Length	At least 12 characters
Uppercase	At least one uppercase letter
Lowercase	At least one lowercase letter
Numbers	At least one numerical digit
Special Characters	At least one special character
Strength Classification
Strength	Criteria Passed
WEAK	0–2 criteria
MEDIUM	3–4 criteria
STRONG	All 5 criteria

Important: Passwords found in the predefined common-password list are automatically classified as WEAK, regardless of their criteria score.

🛠️ Technologies Used
Python 3
Visual Studio Code (VS Code)
string – Character sets and special characters.
secrets – Secure random password generation.
math – Password entropy calculation.
getpass – Hidden password input.
📂 Project Structure
text
Password-Checker/
│
├── main.py
├── README.md
└── .gitignore

🚀 How to Run the Project
1. Clone the Repository
bash
git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the Project Folder
bash
cd Password-Checker

3. Run the Python Program
bash
python main.py


Requirements:

Python 3 installed.
Visual Studio Code or another Python-compatible editor.
No additional external libraries are required.
💻 Example Output
Main Menu
text
===== PASSWORD STRENGTH CHECKER =====

1. Check Password Strength
2. Generate Strong Password
3. Exit

Enter your choice (1-3):

Password Checking – Hide/Show Option
text
Enter your choice (1-3): 1

Password Visibility:
1. Hide password
2. Show password

Choose an option (1-2): 2

Enter password to check: Hello@123456

========== PASSWORD ANALYSIS ==========

Password Strength: STRONG
Criteria Passed: 5 / 5
Estimated Entropy: [calculated value] bits

Good! All five basic criteria are satisfied.

=======================================

Password Generator
text
Enter your choice (1-3): 2

Enter password length (minimum 12): 16

Generated Password: [randomly generated password]

Keep this password somewhere secure.

Common Password Detection
text
Enter your choice (1-3): 1

Password Visibility:
1. Hide password
2. Show password

Choose an option (1-2): 2

Enter password to check: password123

========== PASSWORD ANALYSIS ==========

Password Strength: WEAK

Criteria Passed: 1 / 5

Security Suggestions:
- Use at least 12 characters.
- Add uppercase letters.
- Add special characters.
- Avoid commonly used passwords.

=======================================

Exit Program
text
Enter your choice (1-3): 3

Thank you for using Password Strength Checker!

📐 Password Entropy Formula

The project uses a simplified entropy formula:

H = L × log₂(N)

Where:

H = Estimated password entropy in bits.
L = Password length.
N = Estimated character pool size.

The character pool is determined by the character categories present in the password.

Note: This calculation is only an estimate. It does not account for predictable patterns, repeated characters, or dictionary-based guessing. Therefore, higher estimated entropy does not automatically guarantee a secure password.

🎯 Project Objectives
Understand basic Python programming.
Learn fundamental password security concepts.
Practice conditional statements and loops.
Understand Python functions and modules.
Learn secure random password generation.
Understand basic password entropy calculations.
Practice input validation and error handling.
Develop a simple cybersecurity application.
🔮 Future Improvements
Develop a graphical user interface (GUI) using Tkinter.
Integrate a larger compromised-password database.
Implement Have I Been Pwned API integration using its privacy-preserving k-anonymity approach.
Detect repeated characters and predictable password patterns.
Improve password strength analysis.
Add multilingual support.
Add password history analysis without storing actual passwords.
⚠️ Disclaimer

This project is developed for educational purposes as a beginner cybersecurity project.

The password strength checker provides a basic security assessment and does not guarantee that a password is secure.

The entropy calculator provides a simplified estimate of password randomness.

The common-password detection feature uses a small predefined list and cannot identify every weak or compromised password.

Do not enter real or sensitive passwords into demonstration environments. Avoid sharing generated passwords or storing them in public repositories.

👨‍💻 Author

Developed as a beginner Python cybersecurity project.

⭐ If you find this project useful, feel free to star the repository!
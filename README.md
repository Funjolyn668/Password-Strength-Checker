**🔐 Password Strength Checker**

A beginner-friendly Python cybersecurity project that _checks password strength, generates strong passwords, and provides security suggestions_.

**📌 Project Overview**

This application helps users understand basic password security by checking passwords against five security criteria.

It also includes a password generator, common password detection, an entropy calculator, and a Show/Hide Password option.

**✨ Features**
Password Strength Checker: Rates passwords as WEAK, MEDIUM, or STRONG.
Show/Hide Password: Allows users to choose whether their password is visible while typing.
Password Generator: Creates random passwords using Python's secrets module.
Common Password Detection: Identifies passwords from a predefined list of commonly used passwords.
Entropy Calculator: Estimates password randomness in bits.
Security Suggestions: Provides tips to improve password strength.
Continuous Checking: Allows users to check multiple passwords in one session.

**📊 Password Strength Criteria**
Criteria	Requirement
Length	At least 12 characters
Uppercase	At least one uppercase letter
Lowercase	At least one lowercase letter
Numbers	At least one digit
Special Characters	At least one special character

Strength Classification:
WEAK: Meets 0–2 criteria.
MEDIUM: Meets 3–4 criteria.
STRONG: Meets all 5 criteria.

Common passwords are automatically classified as WEAK.

**🛠️ Technologies Used**
Python 3
Visual Studio Code (VS Code)
string – Character checking.
secrets – Secure password generation.
math – Entropy calculation.
getpass – Hidden password input.

📂 Project Structure
text
Password-Checker/
│
├── main.py
├── README.md
└── .gitignore

**🚀 How to Run**

1. Clone the repository

bash
git clone YOUR_GITHUB_REPOSITORY_URL

2. Navigate to the project folder

bash
cd Password-Checker

3. Run the program

bash
python main.py


Requirements:
Python 3 installed.
No additional external libraries required.

💻 Example Output
text
===== PASSWORD STRENGTH CHECKER =====

1. Check Password Strength
2. Generate Strong Password
3. Exit

Enter your choice (1-3): 1

Password Visibility:
1. Hide password
2. Show password

Choose an option (1-2): 2

Enter password to check: Hello@123456

========== PASSWORD ANALYSIS ==========

Password Strength: STRONG
Criteria Passed: 5 / 5

Good! All five basic criteria are satisfied.

=======================================

**🎯 Project Objectives**
Learn basic Python programming.
Understand password security.
Practice Python functions, loops, and conditions.
Learn secure random password generation.
Understand basic password entropy.
Develop a simple cybersecurity application.

**🔮 Future Improvements**
Add a graphical user interface (GUI) using Tkinter.
Detect more commonly used passwords.
Integrate Have I Been Pwned API.
Improve password security analysis.
Add multilingual support.

**⚠️ Disclaimer**
This project is developed for educational purposes only.

The password checker provides a basic security assessment and does not guarantee password security. The entropy calculation is an estimate, and common password detection uses a limited predefined list.

Do not enter real or sensitive passwords into demonstration environments.

**👨‍💻 Author**
Developed by **Funjolyn** as a beginner Python cybersecurity project.

⭐ If you find this project useful, feel free to star the repository!

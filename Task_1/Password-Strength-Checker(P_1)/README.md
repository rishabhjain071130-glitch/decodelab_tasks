# 🔐 Password Strength Analyzer

> A professional Password Strength Analyzer built using Python for the **DecodeLabs Cyber Security Internship**.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Status](https://img.shields.io/badge/Project-Completed-success.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Cyber Security](https://img.shields.io/badge/Domain-Cyber%20Security-red.svg)

---

## 📖 Overview

Passwords are the first line of defense against cyber attacks. Weak passwords make user accounts vulnerable to brute-force and dictionary attacks.

This project analyzes a password using industry-standard rules and provides a detailed security report including password strength, entropy, estimated crack time, and improvement suggestions.

---

# ✨ Features

- 🔒 Hidden Password Input
- 📊 Password Strength Score (0–100)
- 🎯 Weak / Medium / Strong Classification
- 🔐 Password Entropy Calculation
- 🛡 Estimated Password Crack Time
- 🚫 Common Password Detection
- 🎨 Colorful Terminal Output
- 📈 Animated Progress Bar
- 📋 Password Analysis Report
- 💡 Password Improvement Suggestions
- 🏗 Object-Oriented Python Code
- 📂 Modular Project Structure

---

# 📂 Project Structure

```
Password-Strength-Checker/
│
├── password_checker.py
├── utils.py
├── common_passwords.txt
├── README.md
├── LICENSE
├── requirements.txt
├── .gitignore
├── screenshots/
│   ├── weak.png
│   ├── medium.png
│   └── strong.png
└── assets/
    └── banner.png
```

---

# ⚙ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/Password-Strength-Checker.git
```

Move into the project directory

```bash
cd Password-Strength-Checker
```

Install dependencies

```bash
pip install -r requirements.txt
```

Run the project

```bash
python password_checker.py
```

---

# 🛠 Technologies Used

- Python 3
- Colorama
- Getpass
- Math
- String
- Object-Oriented Programming (OOP)

---

# 📊 Password Evaluation Criteria

| Security Feature | Marks |
|------------------|-------|
| Password Length (8+) | 20 |
| Password Length (12+) | 10 |
| Uppercase Letter | 15 |
| Lowercase Letter | 15 |
| Number | 15 |
| Special Character | 15 |
| High Entropy Bonus | 10 |

Maximum Score = **100**

---

# 📈 Sample Output

```
====================================================
PASSWORD STRENGTH ANALYZER
====================================================

Analyzing Password...

███████████████████████████░░░░ 85%

Password Score : 90 /100

Entropy : 74.62 bits

Estimated Crack Time

Many Years

Password Strength

STRONG

Password Analysis

✓ Length
✓ Uppercase
✓ Lowercase
✓ Number
✓ Special Character

Suggestions

Excellent!
Your password follows strong security practices.
```

---

# 📸 Screenshots

## Weak Password

Save screenshot as

```
screenshots/weak.png
```

---

## Medium Password

Save screenshot as

```
screenshots/medium.png
```

---

## Strong Password

Save screenshot as

```
screenshots/strong.png
```

---

# 🔒 Security Checks

The analyzer checks for

- Minimum password length
- Uppercase letters
- Lowercase letters
- Numbers
- Symbols
- Password entropy
- Common weak passwords

---

# 🎯 Learning Outcomes

By completing this project, I learned

- Password Security Principles
- Object-Oriented Programming
- String Handling
- Conditional Logic
- Cyber Security Fundamentals
- Password Entropy
- Password Strength Evaluation

---

# 🚀 Future Improvements

- GUI using Tkinter
- Dark Mode Interface
- Password Generator
- Password Manager
- Have I Been Pwned API Integration
- Password History Check
- Export Report as PDF

---

# 👨‍💻 Author

**Rishabh Jain**

Cyber Security Intern

DecodeLabs Industrial Training Program (2026)

---

# 📜 License

This project is licensed under the MIT License.

---

⭐ If you like this project, don't forget to give it a star on GitHub.
"""
===========================================================
Utility Functions
Password Strength Analyzer

Author : Rishabh Jain
===========================================================
"""

import math
import string
import time
from colorama import Fore

# -------------------------------
# Password Character Checks
# -------------------------------

def has_uppercase(password):
    return any(c.isupper() for c in password)


def has_lowercase(password):
    return any(c.islower() for c in password)


def has_digit(password):
    return any(c.isdigit() for c in password)


def has_special(password):
    return any(c in string.punctuation for c in password)


# -------------------------------
# Password Score
# -------------------------------

def calculate_score(password):

    score = 0

    if len(password) >= 8:
        score += 20

    if len(password) >= 12:
        score += 10

    if has_uppercase(password):
        score += 15

    if has_lowercase(password):
        score += 15

    if has_digit(password):
        score += 15

    if has_special(password):
        score += 15

    entropy = calculate_entropy(password)

    if entropy >= 60:
        score += 10

    return min(score, 100)


# -------------------------------
# Entropy
# -------------------------------

def calculate_entropy(password):

    pool = 0

    if has_lowercase(password):
        pool += 26

    if has_uppercase(password):
        pool += 26

    if has_digit(password):
        pool += 10

    if has_special(password):
        pool += len(string.punctuation)

    if pool == 0:
        return 0

    entropy = len(password) * math.log2(pool)

    return entropy


# -------------------------------
# Crack Time Estimation
# -------------------------------

def estimate_crack_time(entropy):

    if entropy < 28:
        return "Instantly"

    elif entropy < 36:
        return "Few Minutes"

    elif entropy < 50:
        return "Few Hours"

    elif entropy < 60:
        return "Several Days"

    elif entropy < 70:
        return "Several Months"

    elif entropy < 80:
        return "Many Years"

    else:
        return "Practically Impossible"


# -------------------------------
# Common Password Detection
# -------------------------------

def load_common_passwords():

    try:

        with open(
            "common_passwords.txt",
            "r",
            encoding="utf-8"
        ) as file:

            return set(
                line.strip().lower()
                for line in file
            )

    except FileNotFoundError:

        return set()


COMMON_PASSWORDS = load_common_passwords()


def check_common_password(password, score):

    if password.lower() in COMMON_PASSWORDS:

        return Fore.RED + "VERY WEAK (Common Password)"

    if score <= 40:

        return Fore.RED + "WEAK"

    elif score <= 70:

        return Fore.YELLOW + "MEDIUM"

    else:

        return Fore.GREEN + "STRONG"


# -------------------------------
# Progress Bar
# -------------------------------

def display_progress_bar():

    total = 30

    for i in range(total + 1):

        filled = "█" * i

        empty = "░" * (total - i)

        percent = int((i / total) * 100)

        print(
            f"\r[{filled}{empty}] {percent}%",
            end=""
        )

        time.sleep(0.03)

    print("\n")


# -------------------------------
# Analysis
# -------------------------------

def print_analysis(password):

    print(Fore.CYAN + "\nPassword Analysis")

    print("-" * 40)

    print(
        f"Length (>=8):          {'✓' if len(password)>=8 else '✗'}"
    )

    print(
        f"Length (>=12):         {'✓' if len(password)>=12 else '✗'}"
    )

    print(
        f"Uppercase Letter:      {'✓' if has_uppercase(password) else '✗'}"
    )

    print(
        f"Lowercase Letter:      {'✓' if has_lowercase(password) else '✗'}"
    )

    print(
        f"Number:                {'✓' if has_digit(password) else '✗'}"
    )

    print(
        f"Special Character:     {'✓' if has_special(password) else '✗'}"
    )


# -------------------------------
# Suggestions
# -------------------------------

def print_suggestions(password):

    print(Fore.CYAN + "\nSuggestions")

    print("-" * 40)

    suggestions = []

    if len(password) < 8:
        suggestions.append("Increase password length to at least 8 characters.")

    if len(password) < 12:
        suggestions.append("Use 12 or more characters for better security.")

    if not has_uppercase(password):
        suggestions.append("Add at least one uppercase letter.")

    if not has_lowercase(password):
        suggestions.append("Add at least one lowercase letter.")

    if not has_digit(password):
        suggestions.append("Include at least one number.")

    if not has_special(password):
        suggestions.append("Include at least one special character.")

    if password.lower() in COMMON_PASSWORDS:
        suggestions.append("Avoid using common passwords.")

    if not suggestions:

        print(
            Fore.GREEN +
            "Excellent! Your password follows strong security practices."
        )

    else:

        for item in suggestions:

            print(Fore.YELLOW + "• " + item)
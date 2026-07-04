"""
===========================================================
            PASSWORD STRENGTH ANALYZER
===========================================================

Author      : Rishabh Jain
Internship  : DecodeLabs Cyber Security Internship
Language    : Python 3

Description:
A professional Password Strength Analyzer that evaluates
password security using multiple cybersecurity principles.

Features:
✔ Hidden Password Input
✔ Password Strength Score
✔ Entropy Calculation
✔ Crack Time Estimation
✔ Weak Password Detection
✔ Password Improvement Suggestions
✔ Colorful Terminal Output
===========================================================
"""

import os
import sys
import time
import getpass
from colorama import Fore, Style, init

# Ensure local project directory is on sys.path so utils can be imported
proj_dir = os.path.dirname(os.path.abspath(__file__))
if proj_dir not in sys.path:
    sys.path.insert(0, proj_dir)

try:
    from utils import (
        calculate_score,
        calculate_entropy,
        estimate_crack_time,
        check_common_password,
        display_progress_bar,
        print_analysis,
        print_suggestions
    )
except ImportError as e:
    print(f"Error: Could not import utils module. {e}")
    sys.exit(1)

# Initialize Colorama
init(autoreset=True)


class PasswordStrengthAnalyzer:

    def __init__(self):

        self.password = ""
        self.score = 0
        self.entropy = 0
        self.strength = ""
        self.crack_time = ""

    def clear_screen(self):
        """
        Clears terminal screen.
        """
        os.system("cls" if os.name == "nt" else "clear")

    def banner(self):

        print(Fore.CYAN + "=" * 60)
        print(Fore.GREEN + "          PASSWORD STRENGTH ANALYZER")
        print(Fore.CYAN + "=" * 60)

        print(Fore.YELLOW + "Professional Cyber Security Project")
        print(Fore.YELLOW + "Author : Rishabh Jain")
        print(Fore.CYAN + "=" * 60)

    def get_password(self):

        self.password = getpass.getpass(
            Fore.WHITE + "\nEnter Password : "
        )

    def analyze(self):

        print(Fore.CYAN + "\nAnalyzing password...\n")

        display_progress_bar()

        self.score = calculate_score(self.password)

        self.entropy = calculate_entropy(self.password)

        self.crack_time = estimate_crack_time(self.entropy)

        self.strength = check_common_password(
            self.password,
            self.score
        )

    def show_results(self):

        print("\n")

        print(Fore.CYAN + "-" * 60)

        print(
            Fore.WHITE +
            "Password Score : "
            + Fore.GREEN +
            f"{self.score}/100"
        )

        print(
            Fore.WHITE +
            "Entropy        : "
            + Fore.GREEN +
            f"{self.entropy:.2f} bits"
        )

        print(
            Fore.WHITE +
            "Crack Time     : "
            + Fore.GREEN +
            self.crack_time
        )

        print(
            Fore.WHITE +
            "Strength       : "
            + self.strength
        )

        print(Fore.CYAN + "-" * 60)

        print_analysis(self.password)

        print_suggestions(self.password)

    def run(self):

        self.clear_screen()

        self.banner()

        self.get_password()

        self.analyze()

        self.show_results()


def main():

    analyzer = PasswordStrengthAnalyzer()

    analyzer.run()


if __name__ == "__main__":
    main()
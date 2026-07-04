"""Utilities module containing console UI functions, safety input handlers, and history operations.

This module provides terminal coloring wrappers via colorama, thread-safe CLI loaders,
progress bars, execution timer context managers, input validation loops, history logging
to history.txt, and professional header/footer prints.
"""

import os
import sys
import time
import csv
from datetime import datetime
from contextlib import contextmanager
from typing import Generator, Dict, List, Optional

# Force stdout/stderr to UTF-8 to support Unicode symbols (e.g. loaders and block characters)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

import colorama
from colorama import Fore, Style

# Initialize colorama for cross-platform colored terminal outputs
colorama.init(autoreset=True)


class OperationCancelled(Exception):
    """Exception raised when an operation is cancelled by the user input."""
    pass


# Color shortcuts
def color_text(text: str, color: str) -> str:
    """Wraps text in a Colorama color tag."""
    return f"{color}{text}{Style.RESET_ALL}"


def print_success(msg: str) -> None:
    """Prints a green success message with an indicator."""
    print(f"[{color_text('✓', Fore.GREEN)}] {msg}")


def print_error(msg: str) -> None:
    """Prints a red error message with an indicator."""
    print(f"[{color_text('✗', Fore.RED)}] {msg}")


def print_warn(msg: str) -> None:
    """Prints a yellow warning message with an indicator."""
    print(f"[{color_text('!', Fore.YELLOW)}] {msg}")


def print_info(msg: str) -> None:
    """Prints a cyan info message with an indicator."""
    print(f"[{color_text('i', Fore.CYAN)}] {msg}")


def print_banner() -> None:
    """Prints the professional ASCII Banner for Secure Cipher Studio."""
    banner = f"""
{Fore.CYAN}================================================================================
 ███████ ███████  ██████ ██    ██ ██████  ███████ 
 ██      ██      ██      ██    ██ ██   ██ ██      
 ███████ █████   ██      ██    ██ ██████  █████   
      ██ ██      ██      ██    ██ ██   ██ ██      
 ███████ ███████  ██████  ██████  ██   ██ ███████ 
                                                  
  ██████  ██████  ██   ██ ███████ ██████  
  ██      ██   ██ ██   ██ ██      ██   ██ 
  ██      ██████  ███████ █████   ██████  
  ██      ██      ██   ██ ██      ██   ██ 
  ██████  ██      ██   ██ ███████ ██   ██ 
                                         
  ███████ ████████ ██    ██ ██████  ██  ██████  
  ██         ██    ██    ██ ██   ██ ██ ██    ██ 
  ███████    ██    ██    ██ ██   ██ ██ ██    ██ 
       ██    ██    ██    ██ ██   ██ ██ ██    ██ 
  ███████    ██     ██████  ██████  ██  ██████  
================================================================================{Style.RESET_ALL}
 {Fore.GREEN}Professional Cryptography Toolkit | DecodeLabs Cyber Security Internship{Style.RESET_ALL}
 {Fore.YELLOW}Author: Rishabh Jain | Version: 2.0 | Status: Production Ready{Style.RESET_ALL}
================================================================================
"""
    print(banner)


def print_footer() -> None:
    """Prints a standard toolkit footer."""
    border = color_text("=" * 80, Fore.CYAN)
    credit = color_text("Secure Cipher Studio © 2026. All Cryptographic Operations Localized.", Fore.BLUE)
    print(f"\n{border}\n{credit.center(80)}\n{border}\n")


def get_safe_input(prompt: str, required: bool = True) -> str:
    """Safely retrieves string input from terminal.

    Handles KeyboardInterrupt and EOFError gracefully by raising OperationCancelled.

    Args:
        prompt: The command-line prompt text.
        required: If True, prompt repeats until input is non-empty.

    Returns:
        The cleaned user input string.

    Raises:
        OperationCancelled: If the user cancels execution (Ctrl+C, Ctrl+D).
    """
    try:
        while True:
            val = input(prompt).strip()
            if required and not val:
                print_error("Input cannot be empty. Please enter a valid value (or type 'cancel' to exit).")
                continue
            if val.lower() == 'cancel':
                raise OperationCancelled()
            return val
    except (KeyboardInterrupt, EOFError):
        print()  # Add a newline after the interrupted prompt
        raise OperationCancelled()


def get_validated_int(
    prompt: str, 
    min_val: Optional[int] = None, 
    max_val: Optional[int] = None
) -> int:
    """Safely retrieves and validates an integer input.

    Args:
        prompt: The command-line prompt text.
        min_val: Minimum acceptable value (inclusive).
        max_val: Maximum acceptable value (inclusive).

    Returns:
        A validated integer.

    Raises:
        OperationCancelled: If cancelled by user.
    """
    while True:
        val_str = get_safe_input(prompt, required=True)
        try:
            val = int(val_str)
            if min_val is not None and val < min_val:
                print_error(f"Value must be at least {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print_error(f"Value must be at most {max_val}.")
                continue
            return val
        except ValueError:
            print_error("Invalid integer format. Please try again.")


def get_yes_no(prompt: str) -> bool:
    """Asks the user a binary yes/no question.

    Args:
        prompt: The prompt text.

    Returns:
        True if yes, False if no.
    """
    while True:
        choice = get_safe_input(prompt + " (y/n): ", required=True).lower()
        if choice in ['y', 'yes']:
            return True
        elif choice in ['n', 'no']:
            return False
        else:
            print_error("Please enter 'y' or 'n'.")


@contextmanager
def execution_timer() -> Generator[Dict[str, float], None, None]:
    """Context manager that times the execution of a block of code.

    Yields:
        A dictionary that will contain the 'elapsed_seconds' after the block exits.
    """
    stats = {'elapsed_seconds': 0.0}
    start = time.perf_counter()
    try:
        yield stats
    finally:
        end = time.perf_counter()
        stats['elapsed_seconds'] = end - start


def loading_animation(duration: float = 0.6) -> None:
    """Simulates a cryptographic processing loader.

    Args:
        duration: Time in seconds to run the loader.
    """
    chars = ['◐', '◓', '◑', '◒']
    end_time = time.time() + duration
    i = 0
    sys.stdout.write(f"[{color_text('*', Fore.BLUE)}] Core Engine Processing... ")
    sys.stdout.flush()
    while time.time() < end_time:
        sys.stdout.write(f"\b{chars[i % len(chars)]}")
        sys.stdout.flush()
        time.sleep(0.08)
        i += 1
    sys.stdout.write("\bComplete.\n")
    sys.stdout.flush()


def progress_bar(label: str = "Crunching", steps: int = 15, delay: float = 0.03) -> None:
    """Displays a graphical progress bar.

    Args:
        label: Text prefix for the progress bar.
        steps: Total fill steps.
        delay: Rest interval between steps.
    """
    for i in range(steps + 1):
        percent = (i / steps) * 100
        filled = "█" * i
        empty = "░" * (steps - i)
        sys.stdout.write(f"\r[{color_text('*', Fore.CYAN)}] {label}: [{filled}{empty}] {percent:3.0f}%")
        sys.stdout.flush()
        time.sleep(delay)
    sys.stdout.write("\n")
    sys.stdout.flush()


# History operations
HISTORY_FILE = "history.txt"


def init_history_file() -> None:
    """Creates the history file with CSV header if it doesn't exist."""
    if not os.path.exists(HISTORY_FILE):
        try:
            with open(HISTORY_FILE, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Date", "Time", "Algorithm", "Operation", "Original Text", "Result"])
        except Exception as e:
            print_error(f"Could not initialize history file: {e}")


def log_history(algorithm: str, operation: str, original_text: str, result: str) -> None:
    """Appends a row to the history file.

    Args:
        algorithm: The algorithm used.
        operation: 'Encrypt' or 'Decrypt' (or 'Brute Force').
        original_text: The input text.
        result: The output result.
    """
    init_history_file()
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d")
    time_str = now.strftime("%H:%M:%S")
    
    # Trim texts in history if too large to prevent bloating history.txt
    max_len = 150
    orig_trimmed = original_text[:max_len] + ("..." if len(original_text) > max_len else "")
    res_trimmed = result[:max_len] + ("..." if len(result) > max_len else "")

    try:
        with open(HISTORY_FILE, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([date_str, time_str, algorithm, operation, orig_trimmed, res_trimmed])
    except Exception as e:
        print_error(f"Failed to write to history log: {e}")


def read_history() -> List[List[str]]:
    """Reads all entries from the history log.

    Returns:
        List of entries (each entry is a list of strings).
    """
    init_history_file()
    entries = []
    try:
        with open(HISTORY_FILE, mode='r', newline='', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader, None)  # Skip header
            for row in reader:
                if row:
                    entries.append(row)
    except Exception as e:
        print_error(f"Failed to read history log: {e}")
    return entries


def clear_history() -> None:
    """Removes all history records and resets headers."""
    try:
        with open(HISTORY_FILE, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow(["Date", "Time", "Algorithm", "Operation", "Original Text", "Result"])
        print_success("History cleared successfully.")
    except Exception as e:
        print_error(f"Failed to clear history log: {e}")

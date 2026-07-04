"""Main orchestration file for Secure Cipher Studio.

This module controls the flow of the console application. It displays menus,
handles routing logic, performs cipher operations via delegate calls to cipher.py,
utilizes console elements from utils.py, and catches termination requests cleanly.
"""

import sys
from datetime import datetime
from typing import List, Any

# Force stdout/stderr to UTF-8 to support Unicode symbols (e.g. loaders and block characters)
if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8')
if hasattr(sys.stderr, 'reconfigure'):
    sys.stderr.reconfigure(encoding='utf-8')

# Ensure local directories can be resolved cleanly
from cipher import (
    ALGORITHM_REGISTRY,
    caesar_encrypt,
    caesar_decrypt,
    rot13_encrypt,
    rot13_decrypt,
    atbash_cipher,
    reverse_cipher,
    base64_encode,
    base64_decode,
    xor_encrypt,
    xor_decrypt,
    caesar_brute_force,
    calculate_statistics
)
from utils import (
    OperationCancelled,
    color_text,
    print_banner,
    print_footer,
    print_success,
    print_error,
    print_warn,
    print_info,
    get_safe_input,
    get_validated_int,
    get_yes_no,
    execution_timer,
    loading_animation,
    progress_bar,
    log_history,
    read_history,
    clear_history
)
from colorama import Fore, Style


def display_algorithm_submenu() -> None:
    """Helper method to output the registered encryption/decryption options."""
    print(f"\n{Fore.MAGENTA}--- SELECT ALGORITHM ---{Style.RESET_ALL}")
    for key, algo in ALGORITHM_REGISTRY.items():
        print(f"  {color_text(key, Fore.GREEN)}. {algo['name']} ({color_text(algo['type'], Fore.YELLOW)})")
    print(f"{Fore.MAGENTA}------------------------{Style.RESET_ALL}")


def handle_encrypt() -> None:
    """Orchestrates the encryption workflow."""
    display_algorithm_submenu()
    algo_choice = get_safe_input("Select algorithm (1-6) or type 'cancel': ", required=True)
    if algo_choice not in ALGORITHM_REGISTRY:
        print_error("Invalid algorithm selection. Returning to main menu.")
        return

    algo_meta = ALGORITHM_REGISTRY[algo_choice]
    print_info(f"Selected Cipher: {algo_meta['name']}")

    text = get_safe_input("Enter plaintext to encrypt: ", required=True)

    # Key validation routines if required
    key: Any = None
    if algo_meta['requires_key']:
        key = get_validated_int(
            algo_meta['key_prompt'],
            min_val=algo_meta.get('key_min'),
            max_val=algo_meta.get('key_max')
        )

    # Execution flow with styling and timings
    progress_bar(label=f"Encrypting via {algo_meta['name']}")
    loading_animation(0.4)

    stats_data = calculate_statistics(text)

    with execution_timer() as timer:
        algo_id = algo_meta['id']
        if algo_id == 'caesar':
            result = caesar_encrypt(text, key)
        elif algo_id == 'rot13':
            result = rot13_encrypt(text)
        elif algo_id == 'atbash':
            result = atbash_cipher(text)
        elif algo_id == 'reverse':
            result = reverse_cipher(text)
        elif algo_id == 'base64':
            result = base64_encode(text)
        elif algo_id == 'xor':
            result = xor_encrypt(text, key)
        else:
            print_error("Algorithm driver not found.")
            return

    elapsed_ms = timer['elapsed_seconds'] * 1000.0

    print(f"\n{Fore.GREEN}--- ENCRYPTION SUMMARY ---{Style.RESET_ALL}")
    print(f"Algorithm:      {algo_meta['name']}")
    print(f"Execution Time: {elapsed_ms:.4f} ms")
    print(f"Input Length:   {stats_data['characters']} chars")

    print(f"\n{Fore.YELLOW}Character Statistics:{Style.RESET_ALL}")
    print(f"  Letters: {stats_data['letters']}")
    print(f"  Digits:  {stats_data['digits']}")
    print(f"  Spaces:  {stats_data['spaces']}")
    print(f"  Symbols: {stats_data['symbols']}")

    print(f"\n{Fore.CYAN}Original Plaintext:{Style.RESET_ALL}\n{text}")
    print(f"\n{Fore.GREEN}Encrypted Ciphertext:{Style.RESET_ALL}\n{result}")
    print(f"{Fore.GREEN}--------------------------{Style.RESET_ALL}\n")

    # Logging output
    log_history(
        algorithm=algo_meta['name'],
        operation="Encrypt",
        original_text=text,
        result=result
    )
    print_success("Operation successfully logged to history.")


def handle_decrypt() -> None:
    """Orchestrates the decryption workflow."""
    display_algorithm_submenu()
    algo_choice = get_safe_input("Select algorithm (1-6) or type 'cancel': ", required=True)
    if algo_choice not in ALGORITHM_REGISTRY:
        print_error("Invalid algorithm selection. Returning to main menu.")
        return

    algo_meta = ALGORITHM_REGISTRY[algo_choice]
    print_info(f"Selected Cipher: {algo_meta['name']}")

    text = get_safe_input("Enter ciphertext to decrypt: ", required=True)

    # Key validation routines if required
    key: Any = None
    if algo_meta['requires_key']:
        key = get_validated_int(
            algo_meta['key_prompt'],
            min_val=algo_meta.get('key_min'),
            max_val=algo_meta.get('key_max')
        )

    # Execution flow with styling and timings
    progress_bar(label=f"Decrypting via {algo_meta['name']}")
    loading_animation(0.4)

    try:
        with execution_timer() as timer:
            algo_id = algo_meta['id']
            if algo_id == 'caesar':
                result = caesar_decrypt(text, key)
            elif algo_id == 'rot13':
                result = rot13_decrypt(text)
            elif algo_id == 'atbash':
                result = atbash_cipher(text)
            elif algo_id == 'reverse':
                result = reverse_cipher(text)
            elif algo_id == 'base64':
                result = base64_decode(text)
            elif algo_id == 'xor':
                result = xor_decrypt(text, key)
            else:
                print_error("Algorithm driver not found.")
                return
    except ValueError as val_err:
        print_error(f"Decryption execution failed: {val_err}")
        return

    elapsed_ms = timer['elapsed_seconds'] * 1000.0
    stats_data = calculate_statistics(result)

    print(f"\n{Fore.GREEN}--- DECRYPTION SUMMARY ---{Style.RESET_ALL}")
    print(f"Algorithm:      {algo_meta['name']}")
    print(f"Execution Time: {elapsed_ms:.4f} ms")
    print(f"Output Length:  {stats_data['characters']} chars")

    print(f"\n{Fore.YELLOW}Decrypted Character Statistics:{Style.RESET_ALL}")
    print(f"  Letters: {stats_data['letters']}")
    print(f"  Digits:  {stats_data['digits']}")
    print(f"  Spaces:  {stats_data['spaces']}")
    print(f"  Symbols: {stats_data['symbols']}")

    print(f"\n{Fore.CYAN}Input Ciphertext:{Style.RESET_ALL}\n{text}")
    print(f"\n{Fore.GREEN}Decrypted Plaintext:{Style.RESET_ALL}\n{result}")
    print(f"{Fore.GREEN}--------------------------{Style.RESET_ALL}\n")

    # Logging output
    log_history(
        algorithm=algo_meta['name'],
        operation="Decrypt",
        original_text=text,
        result=result
    )
    print_success("Operation successfully logged to history.")


def handle_brute_force() -> None:
    """Orchestrates Caesar Cipher Brute Force checking all 25 variants."""
    print_info("Initiating Caesar Cipher Brute Force Decryption Mode")
    text = get_safe_input("Enter ciphertext string to brute force: ", required=True)

    progress_bar(label="Generating keyspace solutions")
    loading_animation(0.5)

    with execution_timer() as timer:
        brute_results = caesar_brute_force(text)

    elapsed_ms = timer['elapsed_seconds'] * 1000.0

    print(f"\n{Fore.GREEN}--- CAESAR BRUTE FORCE KEYSPACE ({elapsed_ms:.4f} ms) ---{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'Shift'.center(8)} | {'Decrypted Output Preview'}{Style.RESET_ALL}")
    print("-" * 65)
    for res in brute_results:
        shift_str = f"Shift {res['shift']:02d}"
        preview = str(res['text']).replace('\n', ' ').replace('\r', '')
        # Truncate output length dynamically to fit console standard sizing
        if len(preview) > 50:
            preview = preview[:47] + "..."
        print(f" {shift_str.ljust(7)} | {preview}")
    print("-" * 65)

    log_history(
        algorithm="Caesar Brute Force",
        operation="Brute Force",
        original_text=text,
        result="Keyspace check: shifts 1-25 resolved"
    )
    print_success("Operation successfully logged to history.")


def handle_comparison() -> None:
    """Runs a benchmark utility testing text encryption against all ciphers."""
    print_info("Running Comparative Benchmarking Suite...")
    text = get_safe_input("Enter sample plaintext string: ", required=True)

    progress_bar(label="Running cipher routines")

    comparison_targets = [
        ('Caesar (Shift 3)', lambda: caesar_encrypt(text, 3), 'Low'),
        ('ROT13', lambda: rot13_encrypt(text), 'Low'),
        ('Atbash Cipher', lambda: atbash_cipher(text), 'Low'),
        ('Reverse Cipher', lambda: reverse_cipher(text), 'None'),
        ('Base64 Encode', lambda: base64_encode(text), 'None'),
        ('XOR (Key 42)', lambda: xor_encrypt(text, 42), 'Medium-Low')
    ]

    results = []
    for name, func, sec_level in comparison_targets:
        with execution_timer() as timer:
            out = func()
        # Measure in microseconds for high-precision differences on local CPU operations
        elapsed_us = timer['elapsed_seconds'] * 1_000_000.0
        results.append({
            'name': name,
            'out_len': len(out),
            'time_us': elapsed_us,
            'sec_level': sec_level,
            'sample': out
        })

    print(f"\n{Fore.GREEN}--- CRYPTOGRAPHIC ALGORITHM BENCHMARK ---{Style.RESET_ALL}")
    print(f"{Fore.CYAN}{'Algorithm'.ljust(18)} | {'Out Size'.ljust(8)} | {'Time (µs)'.ljust(12)} | {'Security'.ljust(11)} | {'Output Sample Preview'}{Style.RESET_ALL}")
    print("-" * 90)
    for res in results:
        preview = res['sample'].replace('\n', ' ').replace('\r', '')
        if len(preview) > 30:
            preview = preview[:27] + "..."
        # Format display variables
        name_part = res['name'].ljust(18)
        size_part = str(res['out_len']).rjust(7) + " Chars"
        time_part = f"{res['time_us']:.2f} µs".rjust(12)
        sec_part = res['sec_level'].ljust(11)
        print(f"{name_part} | {size_part} | {time_part} | {sec_part} | {preview}")
    print("-" * 90)
    print_info("Performance metrics may vary based on CPU loads. Operation concluded.")


def handle_info() -> None:
    """Prints comprehensive data about every algorithm in the registry."""
    print(f"\n{Fore.GREEN}--- CIPHER SYSTEM INFORMATION METADATA ---{Style.RESET_ALL}")
    for key in sorted(ALGORITHM_REGISTRY.keys()):
        algo = ALGORITHM_REGISTRY[key]
        print(f"\n{Fore.CYAN}Algorithm:     {algo['name']}{Style.RESET_ALL}")
        print(f"  Type:        {algo['type']}")
        print(f"  Key Matrix:  {algo['key_type']}")
        
        # Colorize security warnings
        sec_str = algo['security_level']
        if 'Low' in sec_str or 'None' in sec_str:
            sec_color = Fore.RED
        else:
            sec_color = Fore.YELLOW
        print(f"  Security:    {color_text(sec_str, sec_color)}")
        print(f"  Description: {algo['description']}")
    print(f"\n{Fore.GREEN}-------------------------------------------{Style.RESET_ALL}")


def handle_view_history() -> None:
    """Reads history log and renders text-based spreadsheet table."""
    print_info("Reading audit log file...")
    rows = read_history()
    if not rows:
        print_warn("Transaction records empty. Perform operations to populate records.")
        return

    print(f"\n{Fore.GREEN}--- HISTORICAL AUDIT TRANSACTIONS ({len(rows)} Records Found) ---{Style.RESET_ALL}")
    
    # Render layout columns
    cols = [
        ("Date", 10),
        ("Time", 8),
        ("Algorithm", 18),
        ("Operation", 10),
        ("Original Text", 20),
        ("Result", 20)
    ]
    separator = "+" + "+".join(["-" * (width + 2) for _, width in cols]) + "+"
    header_parts = [f" {title.ljust(width)} " for title, width in cols]

    print(separator)
    print("|" + "|".join(header_parts) + "|")
    print(separator)

    for row in rows:
        while len(row) < 6:
            row.append("")
        row_parts = []
        for i, val in enumerate(row[:6]):
            width = cols[i][1]
            val_clean = str(val).replace('\n', ' ').replace('\r', '')
            if len(val_clean) > width:
                val_clean = val_clean[:width - 3] + "..."
            row_parts.append(f" {val_clean.ljust(width)} ")
        print("|" + "|".join(row_parts) + "|")
    print(separator)

    # History clean interface
    clear_choice = get_yes_no("Would you like to purge/clear all logged transactions?")
    if clear_choice:
        confirm = get_yes_no("Are you sure? This action is permanent and unrecoverable")
        if confirm:
            clear_history()


def handle_save_report() -> None:
    """Compiles historical transactions into a Markdown report on disk."""
    print_info("Compiling local session metrics...")
    rows = read_history()
    if not rows:
        print_warn("Audit records are empty. Cannot compile a session report.")
        return

    default_name = f"report_{datetime.now().strftime('%Y-%m-%d')}.md"
    filename = get_safe_input(f"Enter target file path (default: {default_name}): ", required=False)
    if not filename:
        filename = default_name

    progress_bar(label="Writing MD report file")

    try:
        with open(filename, mode='w', encoding='utf-8') as f:
            f.write("# Secure Cipher Studio - Audit Certificate Report\n\n")
            f.write(f"**Report Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write("**Internship Unit:** DecodeLabs Cyber Security Division\n")
            f.write("**Lead Security Engineer:** Rishabh Jain\n")
            f.write(f"**Total Logged Transactions:** {len(rows)}\n\n")
            
            f.write("## Cryptographic Operation Log Table\n\n")
            f.write("| Date | Time | Algorithm | Operation | Input Text Snippet | Result Snippet |\n")
            f.write("| --- | --- | --- | --- | --- | --- |\n")
            for row in rows:
                while len(row) < 6:
                    row.append("")
                # Clean elements for markdown compliance
                escaped_row = [str(x).replace('|', '\\|').replace('\n', ' ').replace('\r', '') for x in row[:6]]
                f.write(f"| {escaped_row[0]} | {escaped_row[1]} | {escaped_row[2]} | {escaped_row[3]} | `{escaped_row[4]}` | `{escaped_row[5]}` |\n")

            f.write("\n## Security & Compliance Notice\n")
            f.write("This log represents local operations performed during this session. Key material was stored temporary in volatile memory.\n")
            
        print_success(f"Session audit report compiled successfully and saved to: {filename}")
    except Exception as e:
        print_error(f"Error compiling session report: {e}")


def main() -> None:
    """Core menu system and navigation control loop."""
    print_banner()
    while True:
        try:
            print(f"\n{Fore.BLUE}=== SECURE CIPHER STUDIO MAIN MENU ==={Style.RESET_ALL}")
            print(f"  {color_text('1', Fore.YELLOW)} Encrypt Text")
            print(f"  {color_text('2', Fore.YELLOW)} Decrypt Text")
            print(f"  {color_text('3', Fore.YELLOW)} Caesar Brute Force")
            print(f"  {color_text('4', Fore.YELLOW)} Compare Algorithms")
            print(f"  {color_text('5', Fore.YELLOW)} Cipher Information")
            print(f"  {color_text('6', Fore.YELLOW)} View History")
            print(f"  {color_text('7', Fore.YELLOW)} Save Report")
            print(f"  {color_text('8', Fore.RED)} Exit")
            print(f"{Fore.BLUE}======================================={Style.RESET_ALL}")

            choice = get_safe_input("Select an option (1-8): ", required=True)

            if choice == '1':
                handle_encrypt()
            elif choice == '2':
                handle_decrypt()
            elif choice == '3':
                handle_brute_force()
            elif choice == '4':
                handle_comparison()
            elif choice == '5':
                handle_info()
            elif choice == '6':
                handle_view_history()
            elif choice == '7':
                handle_save_report()
            elif choice == '8':
                print_info("Gracefully shutting down engine. Clearing workspace caches.")
                print_info("Thank you for using Secure Cipher Studio!")
                print_footer()
                sys.exit(0)
            else:
                print_error("Invalid option selection. Please input a number from 1 to 8.")
        
        except OperationCancelled:
            print()
            print_warn("Active process interrupted. Returning safely to Main Menu.")
        except Exception as e:
            print_error(f"Top-level application loop exception caught: {e}")


if __name__ == '__main__':
    main()

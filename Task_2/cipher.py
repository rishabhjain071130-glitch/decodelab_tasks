"""Cipher module containing cryptography algorithms and statistics.

This module provides implementation for Caesar, ROT13, Atbash, Reverse,
Base64, and XOR ciphers. It also features a registry of algorithms and
a text utility that calculates character statistics.
"""

import base64
from typing import Dict, List, Any, Union


def caesar_encrypt(text: str, shift: int) -> str:
    """Encrypts plaintext using the Caesar cipher with a specified shift.

    Args:
        text: The text to encrypt.
        shift: The alphabet shift position.

    Returns:
        The Caesar encrypted string.
    """
    shift = shift % 26
    result = []
    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            result.append(chr((ord(char) - start + shift) % 26 + start))
        else:
            result.append(char)
    return "".join(result)


def caesar_decrypt(text: str, shift: int) -> str:
    """Decrypts ciphertext using the Caesar cipher with a specified shift.

    Args:
        text: The text to decrypt.
        shift: The alphabet shift position.

    Returns:
        The Caesar decrypted string.
    """
    return caesar_encrypt(text, -shift)


def rot13_encrypt(text: str) -> str:
    """Encrypts text using ROT13 (Caesar cipher with key 13).

    Args:
        text: The input string.

    Returns:
        The ROT13 encrypted string.
    """
    return caesar_encrypt(text, 13)


def rot13_decrypt(text: str) -> str:
    """Decrypts text using ROT13 (equivalent to encrypting with 13).

    Args:
        text: The input string.

    Returns:
        The ROT13 decrypted string.
    """
    return caesar_encrypt(text, 13)


def atbash_cipher(text: str) -> str:
    """Encrypts or Decrypts text using the Atbash cipher (symmetric alphabet reflection).

    Args:
        text: The input string.

    Returns:
        The Atbash transformed string.
    """
    result = []
    for char in text:
        if char.isalpha():
            if char.isupper():
                result.append(chr(ord('Z') - (ord(char) - ord('A'))))
            else:
                result.append(chr(ord('z') - (ord(char) - ord('a'))))
        else:
            result.append(char)
    return "".join(result)


def reverse_cipher(text: str) -> str:
    """Reverses the string order.

    Args:
        text: The input string.

    Returns:
        The reversed string.
    """
    return text[::-1]


def base64_encode(text: str) -> str:
    """Encodes UTF-8 text into a Base64 string.

    Args:
        text: Plain text to encode.

    Returns:
        The Base64 encoded ASCII string.
    """
    text_bytes = text.encode('utf-8')
    base64_bytes = base64.b64encode(text_bytes)
    return base64_bytes.decode('utf-8')


def base64_decode(text: str) -> str:
    """Decodes a Base64 string back to UTF-8 text.

    Args:
        text: Base64 string to decode.

    Returns:
        Decoded UTF-8 plaintext.

    Raises:
        ValueError: If the input is not valid Base64 data.
    """
    try:
        # Standardize padding if user entered unpadded Base64
        rem = len(text) % 4
        if rem > 0:
            text += "=" * (4 - rem)
        
        base64_bytes = text.encode('utf-8')
        text_bytes = base64.b64decode(base64_bytes, validate=True)
        return text_bytes.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Invalid Base64 format: {str(e)}")


def xor_encrypt(text: str, key: int) -> str:
    """Encrypts text using byte-wise XOR with a key and returns a hexadecimal string.

    Args:
        text: Plaintext.
        key: Integer key (0-255).

    Returns:
        Hexadecimal string representing the XOR output.
    """
    text_bytes = text.encode('utf-8')
    xor_bytes = bytes(b ^ key for b in text_bytes)
    return xor_bytes.hex()


def xor_decrypt(hex_text: str, key: int) -> str:
    """Decrypts a hexadecimal string using byte-wise XOR with a key.

    Args:
        hex_text: Hexadecimal string representing encrypted bytes.
        key: Integer key (0-255).

    Returns:
        Decoded UTF-8 plaintext.

    Raises:
        ValueError: If the hex_text is invalid or decoding fails.
    """
    try:
        xor_bytes = bytes.fromhex(hex_text)
    except Exception as e:
        raise ValueError(f"Invalid Hexadecimal representation: {str(e)}")
    
    decrypted_bytes = bytes(b ^ key for b in xor_bytes)
    try:
        return decrypted_bytes.decode('utf-8')
    except Exception as e:
        raise ValueError(f"Decryption succeeded, but result is not valid UTF-8. Verify key: {str(e)}")


def caesar_brute_force(text: str) -> List[Dict[str, Union[int, str]]]:
    """Attempts Caesar decryption using all 25 possible shifts.

    Args:
        text: The ciphertext to decrypt.

    Returns:
        A list of dictionaries containing 'shift' and corresponding 'text'.
    """
    results = []
    for shift in range(1, 26):
        decrypted = caesar_decrypt(text, shift)
        results.append({
            'shift': shift,
            'text': decrypted
        })
    return results


def calculate_statistics(text: str) -> Dict[str, int]:
    """Calculates character structure statistics of the text.

    Args:
        text: The text to analyze.

    Returns:
        Dictionary containing counts of characters, letters, digits, spaces, and symbols.
    """
    chars = len(text)
    letters = sum(1 for c in text if c.isalpha())
    digits = sum(1 for c in text if c.isdigit())
    spaces = sum(1 for c in text if c.isspace())
    symbols = chars - (letters + digits + spaces)
    return {
        'characters': chars,
        'letters': letters,
        'digits': digits,
        'spaces': spaces,
        'symbols': symbols
    }


# Algorithm Registry containing metadata for toolkit routing
ALGORITHM_REGISTRY = {
    '1': {
        'id': 'caesar',
        'name': 'Caesar Cipher',
        'type': 'Symmetric Substitution',
        'key_type': 'Integer (Shift Key: 0-25)',
        'description': 'Shifts alphabet characters by a fixed value.',
        'security_level': 'Low (Easily cracked by Brute Force)',
        'requires_key': True,
        'key_prompt': 'Enter Shift Key (0-25): ',
        'key_min': 0,
        'key_max': 25
    },
    '2': {
        'id': 'rot13',
        'name': 'ROT13',
        'type': 'Symmetric Substitution',
        'key_type': 'None (Fixed shift of 13)',
        'description': 'A shift of 13 characters. Self-reciprocal cipher.',
        'security_level': 'Low (Obfuscation only)',
        'requires_key': False
    },
    '3': {
        'id': 'atbash',
        'name': 'Atbash Cipher',
        'type': 'Monoalphabetic Substitution',
        'key_type': 'None (Alphabet reflection)',
        'description': 'Reflected alphabet mapping (A->Z, B->Y).',
        'security_level': 'Low (Obfuscation only)',
        'requires_key': False
    },
    '4': {
        'id': 'reverse',
        'name': 'Reverse Cipher',
        'type': 'Transposition',
        'key_type': 'None',
        'description': 'Reverses the sequence of characters.',
        'security_level': 'None (Obvious format)',
        'requires_key': False
    },
    '5': {
        'id': 'base64',
        'name': 'Base64 Encode/Decode',
        'type': 'Encoding Scheme',
        'key_type': 'None',
        'description': 'Standard binary-to-text encoding scheme.',
        'security_level': 'None (Not a cryptographic cipher)',
        'requires_key': False
    },
    '6': {
        'id': 'xor',
        'name': 'XOR Cipher',
        'type': 'Bitwise Stream Cipher',
        'key_type': 'Integer (8-bit key: 0-255)',
        'description': 'Computes byte-wise XOR, outputting clean hexadecimal.',
        'security_level': 'Medium-Low (Vulnerable if reused/short key)',
        'requires_key': True,
        'key_prompt': 'Enter XOR Numeric Key (0-255): ',
        'key_min': 0,
        'key_max': 255
    }
}

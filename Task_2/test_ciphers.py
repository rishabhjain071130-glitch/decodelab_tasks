"""Automated testing suite for Secure Cipher Studio cryptographic functions.

This module validates encryption, decryption, boundary conditions, error handling,
and round-trip capabilities of Caesar, ROT13, Atbash, Reverse, Base64, and XOR ciphers.
"""

import unittest
from cipher import (
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


class TestCipherSuite(unittest.TestCase):
    """Unit test fixture validating cipher engine functionality."""

    def test_caesar_cipher(self) -> None:
        """Tests Caesar encrypt and decrypt including letter wrapping and symbols."""
        plaintext = "Hello World! 123"
        shift = 5
        ciphertext = caesar_encrypt(plaintext, shift)
        self.assertEqual(ciphertext, "Mjqqt Btwqi! 123")
        
        decrypted = caesar_decrypt(ciphertext, shift)
        self.assertEqual(decrypted, plaintext)

    def test_caesar_boundary_shifts(self) -> None:
        """Tests Caesar cipher with shifting extremes (shift >= 26)."""
        plaintext = "Cryptographic"
        self.assertEqual(caesar_encrypt(plaintext, 26), plaintext)
        self.assertEqual(caesar_encrypt(plaintext, 52), plaintext)
        self.assertEqual(caesar_encrypt(plaintext, 2), caesar_encrypt(plaintext, 28))

    def test_rot13_cipher(self) -> None:
        """Tests ROT13 symmetry and output correctness."""
        text = "Security Engineering 2026"
        encrypted = rot13_encrypt(text)
        self.assertEqual(rot13_decrypt(encrypted), text)
        # Verify specific ROT13 translation
        self.assertEqual(rot13_encrypt("ABC"), "NOP")

    def test_atbash_cipher(self) -> None:
        """Tests Atbash cipher reciprocal logic."""
        text = "Hello, Atbash!"
        encrypted = atbash_cipher(text)
        self.assertEqual(encrypted, "Svool, Zgyzhs!")
        self.assertEqual(atbash_cipher(encrypted), text)

    def test_reverse_cipher(self) -> None:
        """Tests basic string reversing logic."""
        text = "Python Programming"
        self.assertEqual(reverse_cipher(text), "gnimmargorP nohtyP")
        self.assertEqual(reverse_cipher(reverse_cipher(text)), text)

    def test_base64_operations(self) -> None:
        """Tests Base64 encode and decode processes, checking error handling."""
        plaintext = "DecodeLabs Cybersecurity Internship Portfolio 2026!"
        encoded = base64_encode(plaintext)
        decoded = base64_decode(encoded)
        self.assertEqual(decoded, plaintext)

        # Invalid Base64 decoding validation
        with self.assertRaises(ValueError):
            base64_decode("invalid_base64_chars_!@#$")

    def test_xor_operations(self) -> None:
        """Tests XOR bitwise cipher, verifying hex format outputs and decryptions."""
        plaintext = "Super Secret Message!"
        key = 187
        
        encrypted_hex = xor_encrypt(plaintext, key)
        # Ensure it is a valid hex string format
        int(encrypted_hex, 16)
        
        decrypted = xor_decrypt(encrypted_hex, key)
        self.assertEqual(decrypted, plaintext)

        # Invalid hex data decoding validation
        with self.assertRaises(ValueError):
            xor_decrypt("invalid_hex_string_xyz", key)

    def test_caesar_brute_force(self) -> None:
        """Tests brute force generator outputting 25 variants."""
        text = "Khoor"
        results = caesar_brute_force(text)
        self.assertEqual(len(results), 25)
        # Check if the correct decrypt ('Hello' at shift 3) is found
        found_hello = False
        for res in results:
            if res['shift'] == 3 and res['text'] == "Hello":
                found_hello = True
                break
        self.assertTrue(found_hello)

    def test_calculate_statistics(self) -> None:
        """Tests correct calculations of characters, letters, digits, spaces, and symbols."""
        text = "Hello 123!"
        stats = calculate_statistics(text)
        self.assertEqual(stats['characters'], 10)
        self.assertEqual(stats['letters'], 5)
        self.assertEqual(stats['digits'], 3)
        self.assertEqual(stats['spaces'], 1)
        self.assertEqual(stats['symbols'], 1)


if __name__ == '__main__':
    unittest.main()

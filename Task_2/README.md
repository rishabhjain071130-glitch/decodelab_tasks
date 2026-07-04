# Secure Cipher Studio

[![Python Version](https://img.shields.io/badge/python-3.12%2B-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Internship Project](https://img.shields.io/badge/DecodeLabs-Internship-purple.svg)](https://decodelabs.com/)
[![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)]()

A professional, multi-algorithm encryption and decryption toolkit designed in Python. Built as a portfolio project for the **DecodeLabs Cyber Security Internship**, Secure Cipher Studio provides a modular, colorized CLI interface that simplifies the exploration and benchmarking of cryptographic operations.

---

## 📸 Screenshots & Prompts

### Banner Image (`assets/banner.png`)
* **Prompt Used for Generation:** *A professional, high-tech, futuristic cybersecurity banner containing the text 'Secure Cipher Studio'. Clean lines, digital interface elements, lock icons, glowing blue and green binary code grid background, high contrast, modern design, 800x400 resolution.*
* **Location:** `assets/banner.png`

### Terminal Layouts
* **Main Menu Layout (`assets/screenshots/menu.png`):** 
  * *Description:* A sleek terminal viewport containing the ASCII title banner, authorship blocks, and the 8-item navigation menu colored with terminal hues.
* **Encryption Execution (`assets/screenshots/encrypt.png`):** 
  * *Description:* Terminal snapshot displaying the encryption process flow, starting with the progress bar loader and concluding with input stats and the resulting ciphertext.
* **Decryption Verification (`assets/screenshots/decrypt.png`):** 
  * *Description:* Active terminal session showing successful decryption, outputting execution timings in milliseconds alongside character frequency counts.

---

## 🛠️ Features

- **Multi-Algorithm Interface:** Seamlessly switch between Caesar, ROT13, Atbash, Reverse, Base64, and XOR operations.
- **Robust Exception Shield:** Complete terminal protection from user input faults, index overruns, and system terminations (`KeyboardInterrupt` / `EOFError`).
- **Interactive Animations:** Implements threaded loaders, console spinners, and custom dynamic progress bars to mimic state-of-the-art enterprise tools.
- **High-Resolution Performance Profiler:** Measures cipher speeds at microsecond and millisecond levels using high-precision hardware timers.
- **Input Profiler (Statistics):** Analyzes strings for character distributions (letters, digits, symbols, spaces, total count).
- **Persistent Audit Logging:** Saves transactions to a structured local CSV file (`history.txt`) with an interactive view, purge controls, and Markdown report builder.
- **Algorithm Performance Comparison:** Encrypts a sample string against all algorithms simultaneously to generate a performance, compression, and security level comparison matrix.

---

## 📂 Project Structure

```text
Secure-Cipher-Studio/
├── assets/
│   ├── banner.png                  # Project banner graphic
│   └── screenshots/
│       ├── menu.png                # Main menu console preview
│       ├── encrypt.png             # Encryption action preview
│       └── decrypt.png             # Decryption action preview
├── cipher.py                       # Algorithms, registries, and stats engine
├── utils.py                        # Terminal aesthetics, loaders, loggers, and safety inputs
├── main.py                         # Program loop and navigation menu orchestrator
├── test_ciphers.py                 # Automated unit tests for cipher suite validation
├── requirements.txt                # Third-party dependency definitions
├── LICENSE                         # MIT open source license file
├── README.md                       # Product documentation
└── history.txt                     # Local persistent operational log (CSV)
```

---

## 🔐 Supported Algorithms

1. **Caesar Cipher:** Shift-based substitution (Supports custom shifts 0-25).
2. **ROT13:** Symmetrical Caesar Cipher with a hardcoded shift of 13.
3. **Atbash Cipher:** Alphabet reflection mapping (A ↔ Z, B ↔ Y).
4. **Reverse Cipher:** Basic character sequence transposition.
5. **Base64:** Safe ASCII data representation encoding/decoding.
6. **XOR Cipher:** Byte-wise logical exclusive OR encryption (hex output, supports key inputs 0-255).
7. **Caesar Brute Force:** Generates and displays decrypted results for all 25 shift values.

---

## 🚀 Installation & Usage

### Prerequisites
- Python 3.12 or newer installed on your machine.
- Pip (Python Package Installer).

### Setup Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/RishabhJain/Secure-Cipher-Studio.git
   cd Secure-Cipher-Studio
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the Application:**
   ```bash
   python main.py
   ```

---

## 📝 Sample Terminal Output

### Encryption Output Example
```text
=== SECURE CIPHER STUDIO MAIN MENU ===
  1 Encrypt Text
  2 Decrypt Text
  ...
Select an option (1-8): 1

--- SELECT ALGORITHM ---
  1. Caesar Cipher (Symmetric Substitution)
  2. ROT13 (Symmetric Substitution)
  ...
Select algorithm (1-6) or type 'cancel': 1
[i] Selected Cipher: Caesar Cipher
Enter plaintext to encrypt: Hello Cyber World!
Enter Shift Key (0-25): 3

[*] Encrypting via Caesar Cipher: [███████████████] 100%
[*] Core Engine Processing... Complete.

--- ENCRYPTION SUMMARY ---
Algorithm:      Caesar Cipher
Execution Time: 0.0450 ms
Input Length:   18 chars

Character Statistics:
  Letters: 15
  Digits:  0
  Spaces:  2
  Symbols: 1

Original Plaintext:
Hello Cyber World!

Encrypted Ciphertext:
Khoor Fbehu Zruog!
--------------------------

[✓] Operation successfully logged to history.
```

---

## 🔮 Future Scope
- **Advanced Cipher Suites:** Integrating modern block/stream ciphers like AES-256 and ChaCha20.
- **Asymmetric Key Exchange:** Adding support for RSA and Diffie-Hellman algorithms.
- **Hash and HMAC Generators:** Incorporating checksum verifications using SHA-256 and MD5 hashes.
- **Graphical User Interface (GUI):** Developing a PyQt or Tkinter interface for non-technical clients.

---

## ⚖️ License
Distributed under the MIT License. See [LICENSE](file:///d:/Secure%20Cipher%20Studio/LICENSE) for details.

---

## 👨‍💻 Author
**Rishabh Jain**
*DecodeLabs Cyber Security Internship - Portfolio Project*
* **GitHub:** [@RishabhJain](https://github.com/RishabhJain)
* **LinkedIn:** [Rishabh Jain](https://linkedin.com/)

---

## 🏷️ GitHub Topics
`cryptography-toolkit` • `security-engineering` • `caesar-cipher` • `xor-cipher` • `base64-decoder` • `cli-application` • `decodelabs-internship` • `python-project`

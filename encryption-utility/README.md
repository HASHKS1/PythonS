# Encryption/Decryption Utility : Folder & File

This utility provides functions to encrypt and decrypt files and folders using AES encryption. Below you'll find details on how to use the encryption and decryption functions, as well as how the key is managed.

## Table of Contents

1. [Installation](#installation)
2. [Encryption Key Usage](#encryption-key-usage)
3. [Encrypting a File](#encrypting-a-file)
4. [Decrypting a File](#decrypting-a-file)
5. [Encrypting a Folder](#encrypting-a-folder)
6. [Decrypting a Folder](#decrypting-a-folder)
7. [Additional Resources](#additional-resources)

## Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/HASHKS1/PythonS.git
   cd encryption-utility
   ```

2. **Install dependencies:**

   ```bash
   pip3 install -r requirements.txt
   ```

## Encryption Key Usage

The utility uses AES encryption, which requires a key for both encryption and decryption. The key must be of a specific length:

- AES-128: 16 bytes
- AES-192: 24 bytes
- AES-256: 32 bytes

## Encrypting a File

To encrypt a single file, use the encrypt argument:

   ```bash
   python3 encrypt_decrypt.py encrypt demofile.txt
   ```

- The encrypted file will be saved with a .bin extension.
- Example: demofile.txt becomes demofile.txt.bin

Output:

   ```bash
   File encrypted and saved as demofile.txt.bin
   ```

## Decrypting a File

To decrypt a single file, use the decrypt argument:

   ```bash
   python3 encrypt_decrypt.py decrypt demofile.txt.bin
   ```

- The decrypted file will be saved with the original file name.
- Example: demofile.txt.bin will be decrypted back to demofile.txt

Output:

   ```bash
   File decrypted and saved as demofile.txt
   ```

## Encrypting a Folder

To encrypt all files in a folder, use the encrypt argument:

   ```bash
   python3 encrypt_decrypt.py encrypt ./demofolder
   ```

Output:

   ```bash
   ./demofolder/demofile.txt is encrypting.
   File encrypted and saved as ./demofolder/demofile.txt.bin
   ```

## Decrypting a Folder

To decrypt all files in a folder, use the decrypt argument:

   ```bash
   python3 encrypt_decrypt.py decrypt ./demofolder
   ```

Output:

   ```bash
   ./demofolder/demofile.txt.bin is decrypting.
   File decrypted and saved as ./demofolder/demofile.txt
   ```

**Important** : 

This utility is for educational purposes. For production use, ensure to follow best practices for encryption and key management.

## Additional Resources

[AES Encryption & Decryption In Python: Implementation, Modes & Key Management](https://onboardbase.com/blog/aes-encryption-decryption/)
import sys
import os
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import argparse


def encrypt_file(path):
    '''
    Function that take path of a file as argument, and encrypt it using AES-128
    Output of the encrypted file is a ".bin" file.
    '''

    with open(path, 'r') as file:
        plain_text = file.read()

    # The key length must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) Bytes.
    key = b'prvKey0000123445'

    iv = get_random_bytes(AES.block_size)
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    ciphertext = iv + mycipher.encrypt(plain_text.encode())

    # Output the encrypted file
    with open(path + ".bin", "wb") as file_out:
        file_out.write(ciphertext)

    print(f"File encrypted and saved as {path}.bin")

def decrypt_file(path):
    'Function that take path of a ".bin" file as argument, and decrypt it using AES-128'

    with open(path, "rb") as file:
        ciphertext = file.read()

    # The key length must be 16 (AES-128), 24 (AES-192), or 32 (AES-256) Bytes.
    key = b'prvKey0000123445'

    # Extract the IV from the beginning of the ciphertext
    iv = ciphertext[:AES.block_size]

    # Extract the actual ciphertext
    encrypted_text = ciphertext[AES.block_size:]

    # Decrypt the message
    mycipher = AES.new(key, AES.MODE_CFB, iv)
    plain_text = mycipher.decrypt(encrypted_text).decode()

    # Output the decrypted content
    original_file_path = path.replace(".bin", "")
    with open(original_file_path, "w") as file_out:
        file_out.write(plain_text)

    print(f"File decrypted and saved as {original_file_path}")


def encrypt_dir(path):
    """Function that takes the path of a folder as an argument and encrypts all files in it using encrypt_file function."""

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            
            # Optionally, skip already encrypted files
            if file.endswith(".bin"):
                print(file_path + " is already encrypted, skipping.")
                continue
            
            print(file_path + " is encrypting.")
            encrypt_file(file_path)


def decrypt_dir(path):
    """Function that takes the path of a folder as an argument and decrypts all files in it using decrypt_file function."""

    for root, _, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)

            if file.endswith(".bin"):
                print(file_path + " is decrypting.")
                decrypt_file(file_path)
            
            else:
                pass



def main():
    parser = argparse.ArgumentParser(description="Encrypt or Decrypt a folder/file using AES-128")
    parser.add_argument("mode", choices=["encrypt", "decrypt"], help="Mode of operation: Encrypt or Decrypt")
    parser.add_argument("path", help="Path to the folder/file to be encrypted or decrypted")

    args = parser.parse_args()

    if args.mode == "encrypt" and os.path.isdir(args.path) and os.path.exists(args.path):
        encrypt_dir(args.path)
    elif args.mode == "decrypt" and os.path.isdir(args.path) and os.path.exists(args.path):
        decrypt_dir(args.path)
    elif args.mode == "encrypt" and os.path.isfile(args.path) and os.path.exists(args.path):
        encrypt_file(args.path)
    elif args.mode == "decrypt" and os.path.isfile(args.path) and os.path.exists(args.path):
        decrypt_file(args.path)
    else:
        print("Invalid mode. Please choose 'encrypt' or 'decrypt', or check your file")

if __name__ == "__main__":
    main()
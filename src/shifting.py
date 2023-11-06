import sys
from fileConrol import *

plaintext_file = 'plaintext.txt'
encrypted_file = 'encrypted.txt'


def getInput():
    if len(sys.argv) != 2:
        print('python shifting.py <key>')
        sys.exit(1)
    elif len(sys.argv) == 2:
        key = int(sys.argv[1])
        return key
        

def encryptText(input_text):
    encrypted_text = []
    key_str = str(key)
    key_len = len(key_str)

    for i, char in enumerate(input_text):
        if char.isalpha():
            key_index = i % key_len
            key_digit = int(key_str[key_index])

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            encrypted_char = chr((ord(char) - base + key_digit) % 26 + base)
            encrypted_text.append(encrypted_char)
        else:
            encrypted_text.append(char)
    
    return ''.join(encrypted_text)   

def decryptText(input_text):
    decrypted_text = []
    key_str = str(key)
    key_len = len(key_str)

    for i, char in enumerate(input_text):
        if char.isalpha():
            key_index = i % key_len
            key_digit = int(key_str[key_index])

            if char.isupper():
                base = ord('A')
            else:
                base = ord('a')

            decrypted_char = chr((ord(char) - base - key_digit) % 26 + base)
            decrypted_text.append(decrypted_char)
        else:
            decrypted_text.append(char)
    
    return ''.join(decrypted_text)

if __name__ == '__main__':
    checkExists(plaintext_file, encrypted_file)
    #key = getInput()
    key = 982343247823
    plainInput = readFile(plaintext_file)

    encrypted_text = encryptText(plainInput)
    print(f"Encrypted: {encrypted_text}")

    decrypted_text = decryptText(encrypted_text)
    print(f"Decrypted: {decrypted_text}")
    
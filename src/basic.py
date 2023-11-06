import sys
from fileConrol import *

plaintext_file = 'plaintext.txt'
encrypted_file = 'encrypted.txt'

def getInput():
    if len(sys.argv) != 2:
        print('python basic.py <key>')
        sys.exit(1)
    elif len(sys.argv) == 2:
        key = int(sys.argv[1])
        return key

def encryptText(text):
    encrypted_text = ''
    try:
        for char in text:
            encrypted_text += chr(ord(char) + key)
        return encrypted_text
    except Exception as e:
        print(f'Error: {e}')

def decryptText(text):
    decrypted_text = ''
    try:
        for char in text:
            decrypted_text += chr(ord(char) - key)
        return decrypted_text
    except Exception as e:
        print(f'Error: {e}')
            

if __name__ == '__main__':
    checkExists(plaintext_file, encrypted_file)
    #key = getInput()
    key = 2

    plainInput = readFile(plaintext_file)

    encrypted_text = encryptText(plainInput)
    print(f'Encrypted: {encrypted_text}')

    decrypted_text = decryptText(encrypted_text)
    print(f'Decrypted: {decrypted_text}')
    
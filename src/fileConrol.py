def checkExists(plaintext_file, encrypted_file):
    with open(plaintext_file, 'a') as f:
        f.write('')
    #with open(encrypted_file, 'a') as f:
        #f.write('')

def readFile(file):
    with open(file, 'r') as f:
        output = f.read()
        print(f'Read: {output}')
        return output
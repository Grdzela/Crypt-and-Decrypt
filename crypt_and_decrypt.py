import pyAesCrypt

password = input('Enter password for cipher file: ')

# encrypt
# pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)

# decrypt
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)

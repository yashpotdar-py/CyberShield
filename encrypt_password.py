import rsa
import csv

file = open('password_file.csv')
publickey, privatekey = rsa.newkeys(512)
passwords = [row[2] for row in csv.reader(file)]
print(passwords)
encrypted = []
decrypted = []

class Encrypt_Password:

    def encrypt(self):

        
        for password in passwords:
            encrypt =  rsa.encrypt(password.encode(), publickey)
            encrypted.append(encrypt)
        print(encrypted)
    
    def decrypt(self):
        
        for encoded in encrypted:
            decrypt = rsa.decrypt(encoded, privatekey).decode()
            decrypted.append(decrypt)
        print(decrypted)

s = Encrypt_Password()
s.encrypt()
s.decrypt()
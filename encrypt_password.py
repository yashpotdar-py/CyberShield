import rsa
import csv

file = open('password_file.csv')
publickey, privatekey = rsa.newkeys(512)
passwords = [row[2] for row in csv.reader(file)]
encrypted = []
decrypted = []

for password in passwords:
    encrypt =  rsa.encrypt(password.encode(), publickey)
    encrypted.append(encrypt)
    decrypt = rsa.decrypt(encrypt, privatekey).decode()
    decrypted.append(decrypt)

print(passwords)
print(encrypted)
print(decrypted)
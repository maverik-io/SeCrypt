#! /usr/local/bin/python3
import utils

enc = utils.authenticate.Encryption(b'joppu123')

with open('message', 'rb') as file:
    print(enc.decrypt(file.read()))

data = input('Data: ').encode()
data_e = enc.encrypt(data)
print(data_e)
print(enc.decrypt(data_e))

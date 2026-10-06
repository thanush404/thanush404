import random,string

chars = string.punctuation + string.digits + string.ascii_letters
chars = list(chars)

key = chars.copy()

random.shuffle(key)

#ENCRYPT

plain_text = input('Enter A Massege To Encrypt: ')
cipher_text = ''

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f'Original Massege : {plain_text}')
print(f'Encrypted Massege: {cipher_text}')
print()

#DECRYPT

cipher_text = input('Enter A Massege To Decrypt: ')
plain_text = ''

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f'Encrypted Massege: {cipher_text}')
print(f'Decrypted Massege: {plain_text}')
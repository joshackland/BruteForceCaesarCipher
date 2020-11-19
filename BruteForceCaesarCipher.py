#script that brute forces every possible Caesar Cipher combination excluding the original
import string

ALPHABET = string.ascii_uppercase

#Caesar Cipher that works on capitalised letters
def caesar_cipher(text, rot):
    text = text.upper()

    output = ''

    for letter in text:
        if letter in ALPHABET:
            index = (ord(letter) - 65 + rot) % 26
            output += ALPHABET[index]
        else:
            output += letter
    
    return output

cipher_text = input('Enter a Caeser Cipher ciphertext that needs to be brute forced: ')

possible_plaintexts = []

for i in range(1,26):
    possible_plaintexts.append(caesar_cipher(cipher_text, i))

for possible_plaintext in possible_plaintexts:
    print(possible_plaintext)

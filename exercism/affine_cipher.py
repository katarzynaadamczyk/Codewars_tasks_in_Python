''' exercise affine cipher '''

from math import gcd

m = 26

def encode(plain_text, a, b):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    plain_text, ret_val = plain_text.lower(), ''
    for char in plain_text:
        if char.isalpha():
            ret_val += chr(ord('a') + (a * (ord(char) - ord('a')) + b) % m)
        elif char.isdigit():
            ret_val += char        
    return ' '.join([ret_val[i:i+5] for i in range(0, len(ret_val), 5)])


def decode(ciphered_text, a, b):
    if gcd(a, m) != 1:
        raise ValueError("a and m must be coprime.")
    if not ciphered_text.islower():
        raise ValueError("Ciphered text is not lower.")
    ret_val = ''
    for char in ciphered_text:
        if char.isdigit():
            ret_val += char
        elif char.isalpha():
            x = 1
            while ((a * x) % m != 1):
                x += 1
            ret_val += chr(ord('a') + x * (ord(char) - ord('a') - b) % m)
    return ret_val

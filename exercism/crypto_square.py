''' exercise crypto square '''

from math import sqrt

def get_c_r(message_length):
    r = int(sqrt(message_length)) + 1
    c = r if r * r >= message_length else r + 1
    return c, r

def cipher_text(plain_text):
    # clean the text
    new_text = ''
    for char in plain_text:
        if char.isalpha() or char.isdigit():
            new_text += char.lower()
    # count c and r
    c, r = get_c_r(len(new_text))
    print(c, r)
    pass

if __name__ == '__main__':
    print(cipher_text("Chill out."))

''' exercise crypto square '''

from math import sqrt

def get_c_r(message_length):
    r = int(sqrt(message_length))
    if r * (r + 1) < message_length:
        r += 1
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
    print(new_text)
    print(c, r, len(new_text))
    result = [new_text[r_index * c:(r_index + 1) * c].ljust(c) for r_index in range(r)]
    new_result = ['' for _ in range(c)]
    for verse in result:
        for c_index in range(len(verse)):
            new_result[c_index] += verse[c_index]
    return ' '.join(new_result)

if __name__ == '__main__':
    print(cipher_text("Chill out."))
    print(cipher_text('If man was meant to stay on the ground, god would have given us roots.'))

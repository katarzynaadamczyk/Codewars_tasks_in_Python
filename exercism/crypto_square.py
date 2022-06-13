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
    # reshape the text
    new_text = new_text.ljust(r * c)
    # get the result array
    result = [new_text[c_index::c] for c_index in range(c)]
    return ' '.join(result)

if __name__ == '__main__':
    print(cipher_text("Chill out."))
    print(cipher_text('If man was meant to stay on the ground, god would have given us roots.'))

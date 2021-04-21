def add_shift(letter, shift):
    if letter.islower():
        return chr(ord('a') + (ord(letter) + shift - ord('a')) % 26)
    else:
        return chr(ord('A') + (ord(letter) + shift - ord('A')) % 26)


def encode_str(strng, shift):
    runners = 4
    pom = strng[0].lower()
    pom += add_shift(pom, shift) 
    for i in strng:
        if i.isalpha():
            i = add_shift(i, shift)
        pom += i
    ret = []
    fixed_l = len(pom) // runners
    for i in range(runners):
        ret.append(pom[0:fixed_l])
        pom = pom[fixed_l:]
    if pom:
        ret.append(pom)
    return ret



def decode(arr):
    #your code
    pass

def main():
    dec = encode_str('I love you', 2)
    print(dec)
    print(decode(dec))
    dec = encode_str('I should have known that you would have a perfect answer for me!!!', 1)
    print(dec)
    print(decode(dec))


if __name__ == '__main__':
    main()

def encode_str(strng, shift):
    # getting an encoded string
    pom = strng[0].lower()
    pom += chr(ord('a') + (ord(pom) + shift - ord('a')) % 26)
    for i in strng:
        if i.islower():
            i = chr(ord('a') + (ord(i) + shift - ord('a')) % 26)
        elif i.isupper():
            i = chr(ord('A') + (ord(i) + shift - ord('A')) % 26)
        pom += i

    # dividing the message for runners
    runners = 5
    ret = []
    if len(pom) % runners == 0:
        fixed_l = len(pom) // runners
    else:
        fixed_l = len(pom) // runners + 1

    for i in range(runners - 1):
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
    print(len('I love you'))
    print(dec)
    print(decode(dec))
    dec = encode_str('I should have known that you would have a perfect answer for me!!!', 1)
    print(len('I should have known that you would have a perfect answer for me!!!'))
    print(dec)
    print(decode(dec))
    dec = encode_str('O CAPTAIN! my Captain! our fearful trip is done;', 1)
    print(len('O CAPTAIN! my Captain! our fearful trip is done;'))
    print(dec)
    print(decode(dec))
    for i in ["ijJ tipvme ibw", "f lopxo uibu z", "pv xpvme ibwf ", "b qfsgfdu botx", "fs gps nf!!!"]:
        print(len(i))



if __name__ == '__main__':
    main()

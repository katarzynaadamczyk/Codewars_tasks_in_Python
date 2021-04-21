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
    # merging the message and getting the shift
    message = ''
    for i in arr:
        message += i
    shift = ord(message[1]) - ord(message[0])
    if shift < 0:
        shift += 26
    message = message[2:]

    # actual decoding
    ret = ''
    for i in message:
        if i.islower():
            tmp = ord(i) - shift
            if tmp < ord('a'):
                i = chr(ord('z') + tmp - ord('a') + 1)
            else:
                i = chr(tmp)
        elif i.isupper():
            tmp = ord(i) - shift
            if tmp < ord('A'):
                i = chr(ord('Z') + tmp - ord('A') + 1)
            else:
                i = chr(tmp)
        ret += i

    return ret

def main():
    dec = encode_str('I love you', 2)
    print(dec)
    print(decode(dec))
    dec = encode_str('I should have known that you would have a perfect answer for me!!!', 1)
    print(dec)
    print(decode(dec))
    dec = encode_str('O CAPTAIN! my Captain! our fearful trip is done;', 1)
    print(dec)
    print(decode(dec))
    dec = encode_str('zzzZZZ', 3)
    print(dec)
    print(decode(dec))



if __name__ == '__main__':
    main()

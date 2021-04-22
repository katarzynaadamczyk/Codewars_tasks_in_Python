import hashlib
from string import ascii_lowercase
from itertools import product

def password_cracker(hash):

    for passcode in product(ascii_lowercase, repeat=5):
        print("".join(passcode))

    pass

def crack(hash):
    for i in range(100000):
        str2hash = str(i).zfill(5)
        result = hashlib.md5(str2hash.encode())
        if result.hexdigest() == hash:
            return str2hash
    return None

def main():
    out = password_cracker('e6fb06210fafc02fd7479ddbed2d042cc3a5155e')
    print(out) 
    print('Should be "code"')
    out = password_cracker('a94a8fe5ccb19ba61c4c0873d391e987982fbbd3')
    print(out) 
    print('Should be "test"')

if __name__ == '__main__':
    main()
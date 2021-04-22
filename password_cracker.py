import hashlib
from string import ascii_lowercase
from itertools import product

def password_cracker(hash):
    for i in range(1, 10):
        for passcode in product(ascii_lowercase, repeat=i):
            if hashlib.sha1(''.join(passcode).encode()).hexdigest() == hash:
                return ''.join(passcode)
                
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
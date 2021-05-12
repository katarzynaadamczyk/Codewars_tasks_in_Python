import hashlib

def crack(hash):
    for i in range(100000):
        str2hash = str(i).zfill(5)
        if hashlib.md5(str2hash.encode()).hexdigest() == hash:
            return str2hash
    return None

def main():
    out = crack('827ccb0eea8a706c4c34a16891f84e7b')
    print(out) 
    print('Should be 12345')
    out = crack('86aa400b65433b608a9db30070ec60cd')
    print(out) 
    print('Should be 00078')



if __name__ == '__main__':
    main()
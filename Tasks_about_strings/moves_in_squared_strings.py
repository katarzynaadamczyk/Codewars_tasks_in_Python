def rot(strng):
    # your code
    ln = strng.find('\n')
    ret = ''
    for i in range(ln):
        for j in range(ln):
            ret += strng[ln * (ln - i) - 1 - j] # + policzyc dokładnie co dodajemy
        if i < (ln - 1):
            ret += '\n'

    return ret

def selfie_and_rot(strng):
    # your code
    pass

def oper(fct, s):
    # your code
    pass

def main():
    print('abcd\nefgh\nijkl\nmnop')
    print(rot('abcd\nefgh\nijkl\nmnop'))
    pass
    

if __name__ == '__main__':
    main()
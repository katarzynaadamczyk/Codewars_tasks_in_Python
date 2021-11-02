def rot(strng):
    # your code
    ln = strng.find('\n')
    ret = ''
    for i in range(ln):
        for j in range(ln):
            ret += strng[(ln + 1) * (ln - i) - 2 - j] 
        if i < (ln - 1):
            ret += '\n'

    return ret

def selfie_and_rot(strng):
    # your code
    pass

def oper(fct, s):
    return fct(s)

def main():
    print('TESTING rot')
    print('FIRST TEST \n' + rot('abcd\nefgh\nijkl\nmnop') +' should equal \n"ponm\nlkji\nhgfe\ndcba"')
    print('SECOND TEST \n' + rot("fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL") +' should equal \n"LyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif"')
    print('THIRD TEST \n' + rot("rkKv\ncofM\nzXkh\nflCB") +' should equal \n"BClf\nhkXz\nMfoc\nvKkr"')

    pass
    

if __name__ == '__main__':
    main()
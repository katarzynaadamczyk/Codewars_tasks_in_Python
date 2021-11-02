def rot(strng):
    ln = strng.find('\n')
    ret = ''
    for i in range(ln):
        for j in range(ln):
            ret += strng[(ln + 1) * (ln - i) - 2 - j] 
        if i < (ln - 1):
            ret += '\n'

    return ret

def selfie_and_rot(strng):
    ln = strng.find('\n')
    ret = rot(strng)
    for i in range(ln):
        strng = strng[0:(ln * 2 + 1) * i + ln] + '.' * ln + strng[(ln * 2 + 1) * i + ln::]
        ret = ret[0:(ln * 2 + 1) * i] + '.' * ln + ret[(ln * 2 + 1) * i::]
    return strng + '\n' + ret

def oper(fct, s):
    return fct(s)

def main():
    print('TESTING rot\n')
    print('FIRST TEST \n' + rot('abcd\nefgh\nijkl\nmnop') +'\nshould equal \nponm\nlkji\nhgfe\ndcba')
    print('SECOND TEST \n' + rot("fijuoo\nCqYVct\nDrPmMJ\nerfpBA\nkWjFUG\nCVUfyL") +'\nshould equal \nLyfUVC\nGUFjWk\nABpfre\nJMmPrD\ntcVYqC\nooujif')
    print('THIRD TEST \n' + rot("rkKv\ncofM\nzXkh\nflCB") +'\nshould equal \nBClf\nhkXz\nMfoc\nvKkr')

    print('\nTESTING selfie_and_rot\n')
    print('FIRST TEST \n' + selfie_and_rot('abcd\nefgh\nijkl\nmnop') +'\nshould equal \nabcd....\nefgh....\nijkl....\nmnop....\n....ponm\n....lkji\n....hgfe\n....dcba')
    print('SECOND TEST \n' + selfie_and_rot("xZBV\njsbS\nJcpN\nfVnP") +'\nshould equal \nxZBV....\njsbS....\nJcpN....\nfVnP....\n....PnVf\n....NpcJ\n....Sbsj\n....VBZx')
    print('THIRD TEST \n' + selfie_and_rot("uLcq\nJkuL\nYirX\nnwMB") +'\nshould equal \nuLcq....\nJkuL....\nYirX....\nnwMB....\n....BMwn\n....XriY\n....LukJ\n....qcLu')

if __name__ == '__main__':
    main()
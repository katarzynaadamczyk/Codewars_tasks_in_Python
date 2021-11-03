def mix(s1, s2):
    dct1, dct2 = {}, {}
    
    for char in s1:
        dct1.setdefault(char, 0)
        dct1[char] += 1

    for char in s2:
        dct2.setdefault(char, 0)
        dct2[char] += 1

    lst = []

    for key in dct1.keys():
        if key < 'a' or key > 'z' or dct1[key] < 2:
            lst.append(key)
    
    for key in lst:
        del dct1[key]

    lst = []

    for key in dct2.keys():
        if key < 'a' or key > 'z' or dct2[key] < 2:
            lst.append(key)
    
    for key in lst:
        del dct2[key]

    dct1 = dict(sorted(dct1.items(), key=lambda item: item[1], reverse=True))
    dct2 = dict(sorted(dct2.items(), key=lambda item: item[1], reverse=True))

    ret = ''

    #while len(dct1.keys()) > 0 or len(dct2.keys()) > 0:

    #    pass
    print(dct1)
    print(dct2)

    
    return ret



def main():
    print('TESTS:\n')
    print(mix("Are they here", "yes, they are here") + '\nshould equal \n2:eeeee/2:yy/=:hh/=:rr\n')
    print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp") + '\nshould equal \n2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz\n')
    print(mix("looping is fun but dangerous", "less dangerous than coding") + '\nshould equal \n1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg\n')
    print(mix(" In many languages", " there's a pair of functions") + '\nshould equal \n1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt\n')
    print(mix("Lords of the Fallen", "gamekult") + '\nshould equal \n1:ee/1:ll/1:oo\n')
    print('"' + mix("codewars", "codewars") + '"' + '\nshould equal \n""n')
    print('"' + mix("A generation must confront the looming ", "codewarrs") + '"' + '\nshould equal \n"1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"n')
    
    

if __name__ == '__main__':
    main()
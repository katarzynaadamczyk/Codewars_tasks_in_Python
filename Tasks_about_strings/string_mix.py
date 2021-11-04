def create_dict(s): # func to create a dict with lowercase keys and its number of appearances > 1 in given string
    dct = {}
    
    for char in s:
        dct.setdefault(char, 0)
        dct[char] += 1

    lst1 = []

    for key in dct.keys():
        if key < 'a' or key > 'z' or dct[key] < 2:
            lst1.append(key)
    
    for key in lst1:
        del dct[key]
    
    return dct

def mix(s1, s2): 
    dct1 = create_dict(s1)
    dct2 = create_dict(s2)
    sign = ''
    val = 0
    arr = []
    for key in dct1.keys():
        if key in dct2.keys():
            if dct2[key] > dct1[key]:
                sign = '2'
                val = dct2[key]
            elif dct2[key] == dct1[key]:
                sign = '='
                val = dct2[key]
            else:
                sign = '1'
                val = dct1[key]
            del dct2[key]
        else:
            sign = '1'
            val = dct1[key]
        arr.append([key, val, sign])
    for key in dct2.keys():
        arr.append([key, dct2[key], '2'])

    return '/'.join([row[2] + ':' + row[0] * row[1] for row in sorted(arr, key=lambda x: (-x[1], x[2], x[0]))])

def main():
    print('TESTS:\n')
    print(mix("Are they here", "yes, they are here") + '\nshould equal \n2:eeeee/2:yy/=:hh/=:rr\n')
    print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp") + '\nshould equal \n2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz\n')
    print(mix("looping is fun but dangerous", "less dangerous than coding") + '\nshould equal \n1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg\n')
    print(mix(" In many languages", " there's a pair of functions") + '\nshould equal \n1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt\n')
    print(mix("Lords of the Fallen", "gamekult") + '\nshould equal \n1:ee/1:ll/1:oo\n')
    print('"' + mix("codewars", "codewars") + '"' + '\nshould equal \n""')
    print('"' + mix("A generation must confront the looming ", "codewarrs") + '"' + '\nshould equal \n"1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr"')
    
    

if __name__ == '__main__':
    main()
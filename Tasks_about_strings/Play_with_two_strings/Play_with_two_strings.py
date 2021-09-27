def set_dict(s):
    chars = {}
    for char in s.lower():
        chars.setdefault(char, 0)
        chars[char] += 1
    return chars


def change_str(s, dic):
    ret = ''
    for i in s:
        if i.lower() in dic.keys() and dic[i.lower()] % 2:
            if i.islower():
                ret += i.upper()
            else:
                ret += i.lower()
        else:
            ret += i
    return ret

def work_on_strings(a, b):
    chars_a, chars_b = set_dict(a), set_dict(b)
    return change_str(a, chars_b) + change_str(b, chars_a)

def main():
    print(f'{work_on_strings("abc", "cde")} should equal abCCde')
    print(f'{work_on_strings("abcdeFgtrzw", "defgGgfhjkwqe")} should equal abcDeFGtrzWDEFGgGFhjkWqE')
    print(f'{work_on_strings("abcdeFg", "defgG")} should equal abcDEfgDEFGg')
    print(f'{work_on_strings("abab", "bababa")} should equal ABABbababa')


if __name__ == '__main__':
    main()
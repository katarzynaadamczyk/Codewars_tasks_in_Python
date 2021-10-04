def find_pos(tab, element):
    # find right position for element of the table
    if element < tab[0]:
        return 0
    if element >= tab[-1]:
        return len(tab)

    pos = len(tab) // 2
    min = 0
    max = len(tab)

    while True:
        if element >= tab[pos - 1] and element < tab[pos]:
            return pos

        if element < tab[pos]:
            max = pos
        else:
            min = pos

        pos = (min + max) // 2


    return pos

def encode(s):
    if len(s) < 1:
        return ('', 0)
    
    tab, pos = [], 0
    tab.append(s)
    
    for i in range(1, len(s)):
        tmp = s[- i::] + s[:len(s) - i]
        act_pos = find_pos(tab, tmp)
        if (act_pos <= pos):
            pos += 1
        tab.insert(act_pos, tmp)
    
    return (''.join(x[-1] for x in tab), pos)

def decode(s, n):
    if s == '' or n >= len(s) or n < 0:
        return ''
    sorted_letters = ''.join(sorted(s))
    tab = []

    for i in range(len(s)):
        tab.append(s[i] + sorted_letters[i])
    
    tab = sorted(tab)

    for i in range(2, len(s)):
        for j in range(len(tab)):
            tab[j] = s[j] + tab[j]
        tab = sorted(tab)
    
    return tab[n]


def main():
    print(f'Solution for "bananabar" is {encode("bananabar")}, it should equal ("nnbbraaaa", 4)')
    print(f'Solution for "Humble Bundle" is {encode("Humble Bundle")}, it should equal ("e emnllbduuHB", 2)')
    print(f'Solution for "Mellow Yellow" is {encode("Mellow Yellow")}, it should equal ("ww MYeelllloo", 1)')
    print(f'Solution for ("nnbbraaaa", 4) is {decode("nnbbraaaa", 4)}, it should equal "bananabar"')
    print(f'Solution for ("e emnllbduuHB", 2) is {decode("e emnllbduuHB", 2)}, it should equal "Humble Bundle"')
    print(f'Solution for ("ww MYeelllloo", 1) is {decode("ww MYeelllloo", 1)}, it should equal "Mellow Yellow"')


if __name__ == '__main__':
    main()
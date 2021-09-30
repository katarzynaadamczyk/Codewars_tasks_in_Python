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
    return


def main():
    print(f'Solution for "bananabar" is {encode("bananabar")}, it should equal ("nnbbraaaa", 4)')
    print(f'Solution for "Humble Bundle" is {encode("Humble Bundle")}, it should equal ("e emnllbduuHB", 2)')
    print(f'Solution for "Mellow Yellow"" is {encode("Mellow Yellow")}, it should equal ("ww MYeelllloo", 1)')


if __name__ == '__main__':
    main()
def printTable(table):
    
    # define the width of each column
    colwidth = []
    for i in range(len(table)):
        tmp = 0
        for text in table[i]:
            if len(text) > tmp:
                tmp = len(text)
        colwidth.append(tmp)
    
    # print
    for i in range(len(table[0])):
        for j in range(len(table)):
            print(table[j][i].rjust(colwidth[j]), end=' | ')
        print()


def main():
    table = [['jabłka', 'pomarańcze', 'wiśnie', 'banany'],
             ['Alicja', 'Bob', 'Karol', 'Dawid'],
             ['psy', 'koty', 'łosie', 'gęsi']]
    printTable(table)
    

if __name__ == '__main__':
    main()
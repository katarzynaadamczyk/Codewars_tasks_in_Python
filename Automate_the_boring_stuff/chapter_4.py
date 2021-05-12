def return_text(lst_of_things):
    if len(lst_of_things) == 1:
        return str(lst_of_things[0])
    ret = ''
    if len(lst_of_things) > 2:
        for i in lst_of_things[:len(lst_of_things) - 2]:
            ret += str(i) + ', '
    ret += str(lst_of_things[len(lst_of_things) - 2]) + ' and ' + str(lst_of_things[len(lst_of_things) - 1])
    return ret


def main():
    lst = ['apples', 'bananas', 'tofu', 'cats']
    print(lst)
    print(return_text(lst))

if __name__ == '__main__':
    main()
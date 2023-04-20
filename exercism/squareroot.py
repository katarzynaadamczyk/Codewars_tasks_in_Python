''' exercise square root '''

def square_root(number):
    if number < 0:
        return -1
    if number == 0:
        return 0
    min_val, max_val, act_val = 1, number, 1
    while not (act_val ** 2 == number or (act_val ** 2 < number and (act_val + 1) ** 2 > number)):
        if act_val ** 2 < number:
            min_val = act_val
        else:
            max_val = act_val
        act_val = (min_val + max_val) // 2
    return act_val

def main():
    print('test for squareroot: ')
    print('squareroot for 1: ', square_root(1))
    print('squareroot for -1: ', square_root(-1))
    print('squareroot for 10: ', square_root(10))
    print('squareroot for 16: ', square_root(16))
    print('squareroot for 25*25: ', square_root(25*25))


if __name__ == '__main__':
    main()
    
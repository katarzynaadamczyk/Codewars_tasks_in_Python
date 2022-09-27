''' exercise change '''


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target != 0 and target < min(coins):
        raise ValueError("can't make target with given coins")
    ret_val = []
    for coin in sorted(coins, reverse=True):
        while target >= coin:
            ret_val.append(coin)
            target -= coin
    return sorted(ret_val)


def main():
    print(find_fewest_coins([1, 4, 15, 20, 50], 23))
    print('result should be: ', [4, 4, 15])
    
if __name__ == '__main__':
    main()
    
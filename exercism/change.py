''' exercise change '''


def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target != 0 and target < min(coins):
        raise ValueError("can't make target with given coins")
    ret_val, max_coin, min_coin = [], max(coins), min(coins)
   # def find_coins(coins, target, number_of_coins, lst_of_coins):
   #     if number_of_coins == 1 and target not in coins:
   #         return False
   #     
    for number_of_coins in range(target // max_coin + 1, target // min_coin + 1):
        # TODO
        if len(ret_val):
            break
    if target > 0 & len(ret_val) == 0:
        raise ValueError("can't make target with given coins")
    return sorted(ret_val)


def main():
    print(find_fewest_coins([1, 5, 10, 25], 1), 'should equal', [1])
    print(find_fewest_coins([1, 5, 10, 25, 100], 25), 'should equal', [25])
    print(find_fewest_coins([1, 5, 10, 25, 100], 15), 'should equal', [5, 10])
    print(find_fewest_coins([1, 4, 15, 20, 50], 23), 'should equal', [4, 4, 15])
    print(find_fewest_coins([1, 5, 10, 21, 25], 63), 'should equal', [21, 21, 21])
    print(find_fewest_coins([1, 2, 5, 10, 20, 50, 100, 900], 999), 'should equal', [2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    print(find_fewest_coins([2, 5, 10, 20, 50], 21), 'should equal', [2, 2, 2, 5, 10])
    print(find_fewest_coins([4, 5], 27), 'should equal', [4, 4, 4, 5, 5, 5])



if __name__ == '__main__':
    main()
    
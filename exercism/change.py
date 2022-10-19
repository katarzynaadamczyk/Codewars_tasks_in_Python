''' exercise change '''

from copy import deepcopy

def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target != 0 and target < min(coins):
        raise ValueError("can't make target with given coins")
    if target == 0:
        return []
    coins = list(filter(lambda coin: coin <= target, coins))
    calc_table = [[(target + 1, []) for _ in range(target + 1)]]
    for y, coin in enumerate(coins):
        new_line = [(target + 1, [])]
        for i in range(1, target + 1):
            if i >= coin:
                min_coins_so_far = deepcopy(new_line[i - coin])
                if calc_table[y][i][0] >= 1 + len(min_coins_so_far[1]) and sum(min_coins_so_far[1]) + coin == i:
                    min_coins_so_far[1].append(coin)
                    new_line.append((len(min_coins_so_far[1]), min_coins_so_far[1]))
                else:
                    new_line.append(calc_table[y][i])
            else:
                new_line.append(calc_table[y][i])
        calc_table.append(new_line)
   # for line in calc_table:
   #     print(line)
    if sum(calc_table[len(coins)][target][1]) < target:
        raise ValueError("can't make target with given coins")
    return sorted(calc_table[len(coins)][target][1])


def main():
    print(find_fewest_coins([1, 5, 10, 25], 1), 'should equal', [1])
    print(find_fewest_coins([1, 2, 5, 10, 25, 100], 25), 'should equal', [25])
    print(find_fewest_coins([1, 5, 10, 25, 100], 15), 'should equal', [5, 10])
    print(find_fewest_coins([1, 4, 15, 20, 50], 23), 'should equal', [4, 4, 15])
    print(find_fewest_coins([1, 5, 10, 21, 25], 63), 'should equal', [21, 21, 21])
    print(find_fewest_coins([1, 2, 5, 10, 20, 50, 100], 999), 'should equal', [2, 2, 5, 20, 20, 50, 100, 100, 100, 100, 100, 100, 100, 100, 100])
    print(find_fewest_coins([2, 5, 10, 20, 50], 21), 'should equal', [2, 2, 2, 5, 10])
    print(find_fewest_coins([4, 5], 27), 'should equal', [4, 4, 4, 5, 5, 5])



if __name__ == '__main__':
    main()
    
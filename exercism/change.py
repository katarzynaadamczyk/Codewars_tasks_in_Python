''' exercise change '''

from itertools import product

def find_fewest_coins(coins, target):
    if target < 0:
        raise ValueError("target can't be negative")
    if target != 0 and target < min(coins):
        raise ValueError("can't make target with given coins")
    ret_val, number_of_coins = [], 1
   # def find_coins(coins, target, number_of_coins, lst_of_coins):
   #     if number_of_coins == 1 and target not in coins:
   #         return False
   #     
    if target > 0:
        while True:
            print(number_of_coins)
            for lst_of_coins in product(coins, repeat=number_of_coins):
                if sum(lst_of_coins) == target:
                    ret_val = list(lst_of_coins)
                    break
            number_of_coins += 1
    return sorted(ret_val)


def main():
    print(find_fewest_coins([1, 4, 15, 20, 50], 23))
    print('result should be: ', [4, 4, 15])
    
if __name__ == '__main__':
    main()
    
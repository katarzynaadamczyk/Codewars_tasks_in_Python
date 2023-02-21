''' exercise killer sudoku helper '''

from itertools import combinations as comb

def combinations(target, size, exclude):
    result, vals_set = [], set(range(1, 10)).difference(set(exclude))
    for combo in comb(vals_set, size):
        if sum(combo) == target:
            result.append(sorted(list(combo)))
    return result


def main():
    print(combinations(45, 9, []), 'should equal:', [[1,2,3,4,5,6,7,8,9]])
    print(combinations(1, 1, []), 'should equal:', [[1]])

if __name__ == '__main__':
    main()
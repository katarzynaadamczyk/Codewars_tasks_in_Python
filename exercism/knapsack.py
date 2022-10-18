''' exercise knapsack '''

from itertools import combinations

def maximum_value_v1(maximum_weight, items):
    calc_table = [[0 for _ in range(maximum_weight + 1)]]
    for y, item in enumerate(items):
        new_line = [0]
        for i in range(maximum_weight):
            if item["weight"] <= i + 1:
                new_line.append(max(calc_table[y][i+1], item["value"] + calc_table[y][i + 1 - item["weight"]]))
            else:
                new_line.append(max(calc_table[y][i+1], new_line[-1]))
        calc_table.append(new_line)
    for line in calc_table:
        print(line)
    return calc_table[len(items)][maximum_weight]

def maximum_value_v2(maximum_weight, items):
    calc_table = [(0, 0)]
    for i in range(1, len(items) + 1):
        for combo in combinations(items, i):
            calc_table.append((sum([x['weight'] for x in combo]), sum([x['value'] for x in combo])))
    return max(filter(lambda x: x[0] <= maximum_weight, calc_table), key=lambda x: x[1])[1]


def main():
    print(maximum_value_v2(10,
                [
                    {"weight": 2, "value": 5},
                    {"weight": 2, "value": 5},
                    {"weight": 2, "value": 5},
                    {"weight": 2, "value": 5},
                    {"weight": 10, "value": 21},
                ],
            ), 'should equal 21')
    
if __name__ == '__main__':
    main()
    
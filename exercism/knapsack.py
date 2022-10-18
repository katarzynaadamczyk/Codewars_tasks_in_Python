''' exercise knapsack '''

def maximum_value(maximum_weight, items):
    calc_table = [[0 for _ in range(maximum_weight + 1)]]
    for y, item in enumerate(items):
        new_line = [0]
        for i in range(maximum_weight):
          #  print(item)
           # print(new_line)
            if item["weight"] <= i + 1:
                new_line.append(max(calc_table[y][i+1], item["value"] + calc_table[y][i + 1 - item["weight"]]))
            else:
                new_line.append(max(calc_table[y][i+1], new_line[-1]))
        calc_table.append(new_line)
    for line in calc_table:
        print(line)
    return calc_table[len(items)][maximum_weight]


def main():
    print(maximum_value(10,
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
    
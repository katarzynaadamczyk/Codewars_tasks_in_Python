''' exercise rectangles '''

from itertools import combinations

def check_if_down_corresponds(x, down_line):
    for point in down_line:
        pass
    pass

def count_rectangles(upper_line, down_line):
    for upper_index, upper_point in enumerate(upper_line):
        pass
    return 0


def rectangles(strings):
    rect_count, points = 0, []
    for y, line in enumerate(strings):
        if line.count('+') >= 2:
            new_points_line = []
            for x, char in enumerate(line):
                if char == '+':
                    new_points_line.append((y, x))
            if len(new_points_line):
                points.append(new_points_line)
    for upper_line, down_line in combinations(points, 2):
        rect_count += count_rectangles(upper_line, down_line)
    return rect_count


def main():
    test = ["+------+----+",
            "|      |    |",
            "+---+--+    |",
            "|   |       |",
            "+---+-------+"
           ]
    print('Rectangles for test is', rectangles(test), 'while it should equal 3')
    

if __name__ == "__main__":
    main()
    
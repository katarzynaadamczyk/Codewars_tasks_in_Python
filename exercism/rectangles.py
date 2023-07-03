''' exercise rectangles '''

from itertools import combinations
import re

def check_if_down_corresponds(upper_point, down_line, strings):
    for down_point in down_line:
        if down_point[1] == upper_point[1]:
            y_min = min(upper_point[0], down_point[0]) + 1
            y_max = max(upper_point[0], down_point[0])
            if len(re.findall(r'[^|+]', ''.join([strings[y][down_point[1]] for y in range(y_min, y_max)]))) == 0:
                return True
            break
    return False


def check_x_line(point1, point2, strings):
    x_min = min(point1[1], point2[1]) + 1
    x_max = max(point1[1], point2[1])
    if len(re.findall(r'[^-+]', strings[point1[0]][x_min:x_max])) == 0:
        return True
    return False

def count_rectangles(upper_line, down_line, strings):
    count_rect = 0
    for upper_index, upper_point in enumerate(upper_line):
        if check_if_down_corresponds(upper_point, down_line, strings):
            for second_upper_point in upper_line[upper_index+1::]:
                if check_x_line(upper_point, second_upper_point, strings):
                    if check_if_down_corresponds(second_upper_point, down_line, strings) and \
                       check_x_line((down_line[0][0], upper_point[1]), (down_line[0][0], second_upper_point[1]), strings):
                        count_rect += 1
                else:
                    break
    return count_rect


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
        rect_count += count_rectangles(upper_line, down_line, strings)
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
    
''' exercise rectangles '''
# working to shorten code for this exercise
# also on combinations but a little different 
# will get 4 points and check whether they create a rectangle

from itertools import combinations
import re


def check_x_line(point1, point2, strings):
    if len(re.findall(r'[^-+]', strings[point1[0]][point1[1]+1:point2[1]])) == 0:
        return True
    return False

def check_y_line(point1, point2, strings):
    if len(re.findall(r'[^|+]', ''.join([strings[y][point1[1]] for y in range(point1[0] + 1, point2[0])]))) == 0:
        return True
    return False


def count_rectangles(upper_line, down_line, strings):
    count_rect = 0
    for upper_points in combinations(upper_line, 2):
        upper_min = min(upper_points)
        upper_max = max(upper_points)
        if check_x_line(upper_min, upper_max, strings):
            for down_points in combinations(down_line, 2):
                down_min = min(down_points)
                down_max = max(down_points)
                if check_x_line(down_min, down_max, strings) and \
                   upper_min[1] == down_min[1] and upper_max[1] == down_max[1] and \
                   check_y_line(upper_min, down_min, strings) and check_y_line(upper_max, down_max, strings):
                       count_rect += 1
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
    
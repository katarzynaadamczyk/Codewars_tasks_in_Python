'''
My solution to task found on codewars: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

'''

def check_result(result_dict):
    should_be_dict = {4: 1, 3: 2, 2: 3, 1: 4}
    for key in result_dict.keys():
        if key not in should_be_dict.keys() or result_dict[key] != should_be_dict[key]:
            return False
    return True if len(result_dict) == len(should_be_dict) else False

def check_on_x(x1, x2, y, battlefield):
    print(f'check_on_x with params: x1: {x1}, x2:{x2}, y: {y}')
    for x in range(x1, x2 + 1):
        if battlefield[y][x] != 0:
            return False
    return True

def check_on_y(y1, y2, x, battlefield):
    print(f'check_on_y with params: y1: {y1}, y2:{y2}, x: {x}')
    for y in range(y1, y2 + 1):
        if battlefield[y][x] != 0:
            return False
    return True

def check_surroundings(x1, y1, x2, y2, battlefield):
    new_x1 = max(0, x1 - 1)
    new_x2 = min(len(battlefield[0]) - 1, x2 + 1)
    new_y1 = max(0, y1 - 1)
    new_y2 = min(len(battlefield) - 1, y2 + 1)
    
    print(x1, x2)
    print(new_x1, new_x2)
    if y1 != new_y1:
        if not check_on_x(new_x1, new_x2, new_y1, battlefield):
            return False
    if y2 != new_y2:
        if not check_on_x(new_x1, new_x2, new_y2, battlefield):
            return False
    if x1 != new_x1:
        if not check_on_y(new_y1, new_y2, new_x1, battlefield):
            return False
    if x2 != new_x2:
        if not check_on_y(new_y1, new_y2, new_x2, battlefield):
            return False
    return True

def find_len(y, x, battlefield, checked_ones_positions):
    len_y, new_y = 1, y
    while (new_y + 1) < len(battlefield) and battlefield[new_y + 1][x] == 1:
        len_y += 1
        new_y += 1
        checked_ones_positions.add((new_y, x))
    len_x, new_x = 1, x
    while (new_x + 1) < len(battlefield[0]) and battlefield[y][new_x + 1] == 1:
        len_x += 1
        new_x += 1
        checked_ones_positions.add((y, new_x))
    return [len_y, len_x], (y, new_x) if new_x != x else (new_y, x)
        

def validate_battlefield(field):
    ships_count_dict = {}
    checked_ones_positions = set()
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 1:
                if (y, x) in checked_ones_positions:
                    continue
                checked_ones_positions.add((y, x))
                len_x_y, last_pos = find_len(y, x, field, checked_ones_positions)
                if min(len_x_y) == 1:
                    if check_surroundings(x, y, last_pos[1], last_pos[0], field):
                        ships_count_dict.setdefault(max(len_x_y), 0)
                        ships_count_dict[max(len_x_y)] += 1
                    else:
                        return False
                else:
                    return False
            elif field[y][x] != 0:
                return False
    print(ships_count_dict)
    return check_result(ships_count_dict)

def test1():
    battlefield = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
                 [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
                 [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
                 [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
    print('test1')
    print(validate_battlefield(battlefield), 'should be True')
    
def test2():
    field = [
             [0, 0, 0, 1, 0, 0, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 1, 0, 0, 0, 1],
             [0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
             [0, 0, 1, 1, 1, 1, 0, 0, 0, 0],
             [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 1, 0, 0, 0, 0],
             [0, 0, 1, 0, 0, 1, 0, 0, 0, 1]]
    print('test2')
    print(validate_battlefield(field), 'should be True')
    
    
if __name__ == '__main__':
    test1()
    test2()
    
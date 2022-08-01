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
    for x in range(x1, x2 + 1):
        if battlefield[y][x] != 0:
            return False
    return True

def check_on_y(y1, y2, x, battlefield):
    for y in range(y1, y2 + 1):
        if battlefield[y][x] != 0:
            return False
    return True

def check_surroundings(x1, y1, x2, y2, battlefield):
    new_x1 = min(0, x1 - 1)
    new_x2 = max(len(battlefield[0]), x2 + 1)
    new_y1 = min(0, y1 - 1)
    new_y2 = max(len(battlefield), y2 + 1)
    if y1 != new_y1:
        if not check_on_x(new_x1, new_x2, new_y1):
            return False
    if y2 != new_y2:
        if not check_on_x(new_x1, new_x2, new_y2):
            return False
    if x1 != new_x1:
        if not check_on_y(new_y1, new_y2, new_x1):
            return False
    if x2 != new_x1:
        if not check_on_y(new_y1, new_y2, new_x2):
            return False
    return True

def validate_battlefield(field):
    ships_count_dict = {}
    checked_ones_positions = set()
    for y in range(len(field)):
        for x in range(len(field[y])):
            if field[y][x] == 1:
                if (y, x) in checked_ones_positions:
                    continue
                act_len = 1
                checked_ones_positions.add((y, x))
                
                # write your magic here
                ships_count_dict.setdefault(act_len, 0)
                ships_count_dict[act_len] += 1
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
    
if __name__ == '__main__':
    test1()
    
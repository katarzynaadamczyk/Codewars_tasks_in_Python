'''
My solution to task found on codewars: https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

'''

def check_result(result_dict):
    should_be_dict = {4: 1, 3: 2, 2: 3, 1: 4}
    for key in result_dict.keys():
        if key not in should_be_dict.keys() or result_dict[key] != should_be_dict[key]:
            return False
    return True if len(result_dict) == len(should_be_dict) else False

def validate_battlefield(field):
    ships_count_dict = {}
    # write your magic here
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
    
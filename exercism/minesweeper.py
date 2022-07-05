''' exercise minesweeper '''

import re

def check(minefield):
    if len(minefield) > 0:
        line_len = len(minefield[0])
        for line in minefield:
            if len(line) != line_len or not re.match(r'^[ *]*$', line):
                return True
    return False

def annotate(minefield):
    if check(minefield):
        raise ValueError("The board is invalid with current input.")
    result = []
    for x in range(len(minefield)):
        tmp = ''
        for y in range(len(minefield[x])):
            if minefield[x][y] == '*':
                tmp += '*'
            else:
                act_count = 0
                for x2 in range(max(x-1, 0), min(x+2, len(minefield))):
                    act_count += minefield[x2][max(0, y-1):min(len(minefield[x2]), y+2)].count('*')
                tmp += str(act_count) if act_count > 0 else ' '
        result.append(tmp)
    return result

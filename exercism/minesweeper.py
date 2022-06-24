''' exercise minesweeper '''

import re

def check(minefield):
    if len(minefield) > 0:
        line_len = len(minefield[0])
        for line in minefield:
            if len(line) != 0 or re.match(r'^[ *]', line):
                return True
    return False

def annotate(minefield):
    if check(minefield):
        raise ValueError("The board is invalid with current input.")
    result = []
    for x in range(len(minefield)):
        tmp = []
        for y in range(len(minefield[x])):
            if minefield[x][y] == '*':
                tmp.append('*')
            else:
                act_count = 0
                for x2 in range(min(x-1, 0), max(x+2, len(minefield))):
                    for y2 in range(min(y-1, 0), max(y+2, len(minefield[x]))):
                        if minefield[x2][y2] == '*':
                            act_count += 1
                result.append(act_count if act_count > 0 else ' ')
            result.append(tmp)
    return result
'''
exercise spiral matrix
done after spiralize from play with arrays

    spiral = [[0 for _ in range(size)] for _ in range(size - 1)]
    spiral.insert(0, [1 for _ in range(size)])
    new_direction = DIRECTION * ((size - 1) // 4) + DIRECTION[0:((size - 1) % 4)]
    y, x, act_len = 0, size - 1, size - 1
    for i, direction in enumerate(new_direction):
        for _ in range(act_len):
            y += direction[0]
            x += direction[1]
            spiral[y][x] = 1        
        if i % 2 == 1:
            act_len -= 2
        if act_len == 0:
            break
    return spiral

'''


DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)
RIGHT = (0, 1)

DIRECTION = [DOWN, LEFT, UP, RIGHT]

def spiral_matrix(size):
    spiral = [[0 for _ in range(size)] for _ in range(size - 1)]
    spiral.insert(0, [x + 1 for x in range(size)])
    act_val, act_len, y, x = size, size - 1, 0, size - 1
    new_direction = DIRECTION * size
    for i, direction in enumerate(new_direction):
        for _ in range(act_len):
            y += direction[0]
            x += direction[1]
            act_val += 1
            spiral[y][x] = act_val
        if i % 2 == 1:
            act_len -= 1
        if act_len == 0:
            break
    return spiral

if __name__ == '__main__':
    spiral = spiral_matrix(4)
    for line in spiral:
        print(line)
    
    spiral = spiral_matrix(10)
    for line in spiral:
        print(line)
        
'''
my solution to problem found on : https://www.codewars.com/kata/534e01fbbb17187c7e0000c6/

'''



DOWN = (1, 0)
LEFT = (0, -1)
UP = (-1, 0)
RIGHT = (0, 1)

DIRECTION = [DOWN, LEFT, UP, RIGHT]

def spiralize(size):
    # Make a snake
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

def test1():
    print('test1')
    print(spiralize(5))
    should_be = [[1,1,1,1,1],
                 [0,0,0,0,1],
                 [1,1,1,0,1],
                 [1,0,0,0,1],
                [1,1,1,1,1]]
    print('should be: ')
    print(should_be)
    
def test2():
    print('test2')
    print(spiralize(8))
    should_be = [[1,1,1,1,1,1,1,1],
                 [0,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,0,1],
                 [1,0,0,0,0,1,0,1],
                 [1,0,1,0,0,1,0,1],
                 [1,0,1,1,1,1,0,1],
                 [1,0,0,0,0,0,0,1],
                 [1,1,1,1,1,1,1,1]]
    print('should be: ')
    print(should_be)
    
if __name__ == '__main__':
    test1()
    test2()
    
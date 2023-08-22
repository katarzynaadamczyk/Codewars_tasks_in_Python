'''

my solution to task: https://leetcode.com/problems/spiral-matrix/

'''

from itertools import cycle
from typing import List

class Solution:
    
    LEFT = (0, 1)
    RIGHT = (0, -1)
    DOWN = (1, 0)
    UP = (-1, 0)
    
    DIRECTIONS = [LEFT, DOWN, RIGHT, UP]
    
    
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        max_x, max_y = len(matrix[0]), len(matrix)
        result, x, y, max_len = [], -1, 0, max_x * max_y
        min_x, min_y = -1, -1
        act_direction = Solution.UP
        while len(result) != max_len:
            act_direction = Solution.DIRECTIONS[(Solution.DIRECTIONS.index(act_direction) + 1) % 4]
            while min_x < x + act_direction[1] < max_x and min_y < y + act_direction[0] < max_y:
                x += act_direction[1]
                y += act_direction[0]
                result.append(matrix[y][x])
            if act_direction == Solution.UP:
                min_x += 1
            elif act_direction == Solution.DOWN:
                max_x -= 1
            elif act_direction == Solution.LEFT:
                min_y += 1
            else:
                max_y -= 1
        return result
    
def main():
    sol = Solution()
    
    print(sol.spiralOrder([[1,2,3],[4,5,6],[7,8,9]]), 'should equal [1,2,3,6,9,8,7,4,5]')
    
if __name__ == '__main__':
    main()
    
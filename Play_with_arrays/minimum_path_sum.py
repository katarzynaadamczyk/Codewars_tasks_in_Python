'''
my solution to: 
https://leetcode.com/problems/minimum-path-sum/
'''

from queue import PriorityQueue
from sys import maxsize
from typing import List, Tuple


class Solution:        
    def minPathSum(self, grid: List[List[int]]) -> int:
        path, row = [], [grid[0][0]]
        for value in grid[0][1:]:
            row.append(row[-1] + value)
        path.append(row)
        for line in grid[1:]:
            row = [line[0] + path[-1][0]]
            for x, value in enumerate(line[1:], start=1):
                row.append(min(row[-1], path[-1][x]) + value)
            path.append(row)
        return path[-1][-1]
            
    
# getting solution if all moves are acceptable
class Solution2(Solution):
    def getPossiblePositions(self, act_y: int, act_x: int) -> Tuple[int, int, int]: 
        if act_y - 1 >= 0:
            yield self.grid[act_y - 1][act_x], act_y - 1, act_x
        if act_y + 1 <= self.goal[0]:
            yield self.grid[act_y + 1][act_x], act_y + 1, act_x
        if act_x - 1 >= 0:
            yield self.grid[act_y][act_x - 1], act_y, act_x - 1
        if act_x + 1 <= self.goal[1]:
            yield self.grid[act_y][act_x + 1], act_y, act_x + 1
    
    def getManhattanDistanceToGoal(self, act_y: int, act_x: int) -> int:
        return (self.goal[0] - act_y) + (self.goal[1] - act_x) 

    def prepareCheckGrid(self):
        self.check_grid = [[maxsize for _ in range(len(self.grid[0]))] for _ in range(len(self.grid))]
            
    def minPathSum(self, grid: List[List[int]]) -> int:
        self.grid = grid
        self.goal = (len(grid) - 1, len(grid[0]) - 1) # (y, x)
        self.prepareCheckGrid()
        stack = PriorityQueue()
        stack.put((self.grid[0][0], sum(self.goal), 0, 0)) # put act_value, manhattan_distance to goal, act_y, act_x
        while not stack.empty():
            act_value, _, act_y, act_x = stack.get()
            if (act_y, act_x) == self.goal:
                return act_value
            if act_value < self.check_grid[act_y][act_x]:
                self.check_grid[act_y][act_x] = act_value
                for value, y, x in self.getPossiblePositions(act_y, act_x):
                    stack.put((act_value + value, self.getManhattanDistanceToGoal(y, x), y, x))
        return 0

def test(solution: Solution, grid: List[List[int]], result: int) -> bool:
        act_result = solution.minPathSum(grid)
        if act_result == result:
            print('ok')
            print('{} equals {}'.format(act_result, result))
            return True
        print('NOK')
        print('{} should equal {}'.format(act_result, result))
        return False



def main():
    sol = Solution()
    sol2 = Solution2()
    
    # test 1
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    test(sol, grid, 7)
    test(sol2, grid, 7)
    
    # test 2
    grid = [[1,2,3],[4,5,6]]
    test(sol, grid, 12)
    test(sol2, grid, 12)
    
    # test 3
    grid = [[5,4,2,9,6,0,3,5,1,4,9,8,4,9,7,5,1],[3,4,9,2,9,9,0,9,7,9,4,7,8,4,4,5,8],[6,1,8,9,8,0,3,7,0,9,8,7,4,9,2,0,1],[4,0,0,5,1,7,4,7,6,4,1,0,1,0,6,2,8],\
            [7,2,0,2,9,3,4,7,0,8,9,5,9,0,1,1,0],[8,2,9,4,9,7,9,3,7,0,3,6,5,3,5,9,6],[8,9,9,2,6,1,2,5,8,3,7,0,4,9,8,8,8],[5,8,5,4,1,5,6,6,3,3,1,8,3,9,6,4,8],\
            [0,2,2,3,0,2,6,7,2,3,7,3,1,5,8,1,3],[4,4,0,2,0,3,8,4,1,3,3,0,7,4,2,9,8],[5,9,0,4,7,5,7,6,0,8,3,0,0,6,6,6,8],[0,7,1,8,3,5,1,8,7,0,2,9,2,2,7,1,5],\
            [1,0,0,0,6,2,0,0,2,2,8,0,9,7,0,8,0],[1,1,7,2,9,6,5,4,8,7,8,5,0,3,8,1,5],[8,9,7,8,1,1,3,0,1,2,9,4,0,1,5,3,1],[9,2,7,4,8,7,3,9,2,4,2,2,7,8,2,6,7],\
            [3,8,1,6,0,4,8,9,8,0,2,5,3,5,5,7,5],[1,8,2,5,7,7,1,9,9,8,9,2,4,9,5,4,0],[3,4,4,1,5,3,3,8,8,6,3,5,3,8,7,1,3]]
    test(sol, grid, 82)
    test(sol2, grid, 79)

if __name__ == '__main__':
    main()

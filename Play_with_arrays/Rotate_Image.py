'''

my solution to problem: https://leetcode.com/problems/rotate-image/

'''

from typing import List

class Solution:
    left = lambda n, x, y: ((y + x) % n, n - x - 1)
    down = lambda n, x, y: (n - y - 1, x - y) # TODO
    right = lambda n, x, y: (y + x, n - x - 1) # TODO
    up = lambda n, x, y: ((n - y - 1) % n, (x - y) % n) # TODO
    
    directions = [left] #, down, right, up]
    
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for index in range(i, n - i):
                act_x, act_y, tmp = index, index, matrix[index][index]
                print(tmp)
                for dir in Solution.directions:
                    new_y, new_x = dir(n, act_x, act_y)
                    matrix[new_y][new_x], tmp = tmp, matrix[new_y][new_x]
        


def main():
    sol = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    sol.rotate(matrix)
    print(matrix, 'should equal:', [[7,4,1],[8,5,2],[9,6,3]])
  #  matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
  #  sol.rotate(matrix)
  #  print(matrix, 'should equal:', [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
    
if __name__ == '__main__':
    main()
    
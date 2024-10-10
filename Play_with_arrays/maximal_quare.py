'''
my solution to task:
https://leetcode.com/problems/maximal-square


'''
from typing import List
from queue import Queue

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # returning if table does not exist or is empty
        if matrix is None or len(matrix) < 1:
            return 0
        # create dp_table
        dp_table = [[int(x) for x in row] for row in matrix]
        # keep in mind max length of square side
        self.max_val = max(max(dp_table[0]), max([row[0] for row in dp_table]))
        # save m & n values to variables
        rows, cols = len(matrix), len(matrix[0])
        # proceed on dp table
        for i in range(1, rows):
            for j in range(1, cols):
                if dp_table[i][j] == 1:
                    dp_table[i][j] += min(dp_table[i-1][j], dp_table[i-1][j-1], dp_table[i][j-1])
                    self.max_val = max(dp_table[i][j], self.max_val)

        return self.max_val ** 2

def main():
    sol = Solution()
    # test 1
    rectangle = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
    print(sol.maximalSquare(rectangle), 'should equal 4')
    
    
    # test 2
    rectangle = [["0","1"],["1","0"]]
    print(sol.maximalSquare(rectangle), 'should equal 1')


    # test 3
    rectangle = [["0"]]
    print(sol.maximalSquare(rectangle), 'should equal 0')
    

if __name__ == '__main__':
    main()
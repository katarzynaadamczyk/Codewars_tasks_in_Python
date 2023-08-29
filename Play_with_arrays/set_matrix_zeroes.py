'''
my solution to task: https://leetcode.com/problems/set-matrix-zeroes/
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # find all zeroes
        y_set, x_set = set(), set()
        for y, row in enumerate(matrix):
            for x, value in enumerate(row):
                if value == 0:
                    y_set.add(y)
                    x_set.add(x)
        
        m, n = len(matrix), len(matrix[0])
        for y in y_set:
            for x in range(n):
                matrix[y][x] = 0
        for x in x_set:
            for y in range(m):
                matrix[y][x] = 0
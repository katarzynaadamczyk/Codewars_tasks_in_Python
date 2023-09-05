'''

my solution to task on LeetCode: https://leetcode.com/problems/valid-sudoku/

'''

from typing import List

class Solution:
    def isValidRow(self, row: List[str]) -> bool:
        new_row = [x for x in row if x.isdigit()]
        return len(new_row) == len(set(new_row))
    
    def isValidThisBoard(self, board: List[List[str]]) -> bool:
        for row in board:
            if self.isValidRow(row) is False:
                return False
        return True

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        return self.isValidThisBoard(board) and self.isValidThisBoard([[row[i] for row in board]\
             for i in range(len(board))]) and self.isValidThisBoard([board[i][j:j+3] + board[i+1][j:j+3] +\
             board[i+2][j:j+3] for j in range(0, len(board), 3) for i in range(0, len(board), 3)])



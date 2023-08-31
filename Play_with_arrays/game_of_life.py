'''

my solution to game of life problem:
https://leetcode.com/problems/game-of-life/

'''

from typing import List, Set, Tuple

class Solution:
    def getChangedStates(self, board: List[List[int]]) -> Set[Tuple[int, int]]:
        m, n = len(board), len(board[0])
        setXY = set()
        for y in range(m):
            for x in range(n):
               # print([sum(board[i][max(0, x - 1):x+1]) for i in range(max(0, y-1), min(y+2, m))])
                actSum = sum([sum(board[i][max(0, x - 1):min(x+2, n)]) for i in range(max(0, y-1), min(y+2, m))]) - board[y][x]
                if (board[y][x] == 1 and actSum not in [2, 3]) or (board[y][x] == 0 and actSum == 3):
                    setXY.add((x, y))
                    print(actSum, board[y][x])
                    print(x, y)
        return setXY            
            
    
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        for x, y in self.getChangedStates(board):
            board[y][x] = 0 if board[y][x] == 1 else 1
        

def main():
    matrix = [[1, 1], [1, 0]]
    print(matrix)
    sol = Solution()
    sol.gameOfLife(matrix)
    print('first test')
    print(matrix)
    
    matrix = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    print(matrix)
    sol.gameOfLife(matrix)
    print('second test')
    print(matrix)
    
if __name__ == '__main__':
    main()
        
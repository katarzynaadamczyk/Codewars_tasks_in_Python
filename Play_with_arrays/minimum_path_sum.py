'''
my solution to: 
https://leetcode.com/problems/minimum-path-sum/
'''

from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pass
    
def main():
    sol = Solution()
    
    # test 1
    grid = [[1,3,1],[1,5,1],[4,2,1]]
    print(sol.minPathSum(grid), 'should equal 7')
    
    # test 2
    grid = [[1,2,3],[4,5,6]]
    print(sol.minPathSum(grid), 'should equal 12')


if __name__ == '__main__':
    main()

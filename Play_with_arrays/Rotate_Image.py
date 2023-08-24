'''

my solution to problem: https://leetcode.com/problems/rotate-image/

'''

from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """


def main():
    sol = Solution()
    print(sol.rotate([[1,2,3],[4,5,6],[7,8,9]]), 'should equal:', [[7,4,1],[8,5,2],[9,6,3]])
    print(sol.rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]), 'should equal:', [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
    
if __name__ == '__main__':
    main()
    
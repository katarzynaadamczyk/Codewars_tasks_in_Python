'''

my solution to problem: https://leetcode.com/problems/triangle/

'''
from queue import PriorityQueue
from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        stack = PriorityQueue()
        act_sum, act_y, triangle_len = triangle[0][0], 0, len(triangle)
        stack.put((-1 * act_y, act_sum, 0))
        while not stack.empty():
            act_y, act_sum, act_x = stack.get()
            act_y = - 1 * act_y
            if act_y + 1 == triangle_len:
                return act_sum
            stack.put((-1 * (act_y + 1), act_sum + triangle[act_y + 1][act_x], act_x))
            stack.put((-1 * (act_y + 1), act_sum + triangle[act_y + 1][act_x + 1], act_x + 1))
        return 0

def main():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    for row in triangle:
        print(row)
    sol = Solution()
    print(sol.minimumTotal(triangle), 'should equal 11')
    triangle = [[-1],[2,3],[1,-1,-3]]
    for row in triangle:
        print(row)
    sol = Solution()
    print(sol.minimumTotal(triangle), 'should equal -1')
    

if __name__ == '__main__':
    main()
    
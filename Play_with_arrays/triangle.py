'''

my solution to problem: https://leetcode.com/problems/triangle/

'''
from typing import List

class Solution:        
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        act_sums = [0]
        for index, row in enumerate(triangle):
            new_sums = []
            for x, value in enumerate(row):
                if x == 0:
                    new_sums.append(value + act_sums[x])
                elif x == index:
                    new_sums.append(value + act_sums[-1])
                else:
                    new_sums.append(value + min(act_sums[x - 1], act_sums[x]))
            act_sums = new_sums
        return min(act_sums)

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
    
    triangle = [[-7],[-2,1],[-5,-5,9],[-4,-5,4,4],[-6,-6,2,-1,-5],[3,7,8,-3,7,-9],[-9,-1,-9,6,9,0,7],[-7,0,-6,-8,7,1,-4,9],[-3,2,-6,-9,-7,-6,-9,4,0],[-8,-6,-3,-9,-2,-6,7,-5,0,7],[-9,-1,-2,4,-2,4,4,-1,2,-5,5],[1,1,-6,1,-2,-4,4,-2,6,-6,0,6],[-3,-3,-6,-2,-6,-2,7,-9,-5,-7,-5,5,1]]
    for row in triangle:
        print(row)
    sol = Solution()
    print(sol.minimumTotal(triangle), 'should equal -63')
    
    

if __name__ == '__main__':
    main()
    
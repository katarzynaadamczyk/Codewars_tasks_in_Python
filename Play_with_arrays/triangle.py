'''

my solution to problem: https://leetcode.com/problems/triangle/

'''

from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        act_sums = [0]
        for y, row in enumerate(triangle):
            new_sums = []
            for i, value in enumerate(act_sums):
                new_sums.append(row[i] + value)
                if i < y:
                    new_sums.append(row[i + 1] + value)
            act_sums = new_sums
            print(act_sums)
        return min(act_sums)

def main():
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    sol = Solution()
    print(sol.minimumTotal(triangle), 'should equal 11')
    

if __name__ == '__main__':
    main()
    
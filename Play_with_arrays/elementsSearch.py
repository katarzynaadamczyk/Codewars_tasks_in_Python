'''
my solution to problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not target in nums:
            return [-1, -1]
        min_i, max_i = 0, len(nums) - 1
        max_avg_i = min_avg_i = (min_i + max_i) // 2
        print(max_avg_i, min_avg_i)
        
    
def main():
    sol = Solution()
    # test 1
    nums = [5,7,7,8,8,10]
    target = 8
    print(sol.searchRange(nums, target), 'should equal [3,4]')


if __name__ == '__main__':
    main()
    
'''
my solution to problem: https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
'''

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        max_val = len(nums) - 1
        min_i, max_i = 0, max_val
        if nums[min_i] == nums[max_i] and nums[max_i] == target:
            return [min_i, max_i]
        if nums[min_i] == target:
            avg_i = min_i
        elif nums[max_i] == target and nums[max_i - 1] < target:
            avg_i = max_i
        else:
            avg_i = (min_i + max_i) // 2
        result = []
        # search for first occurence of target
        while avg_i > 0 and avg_i < max_val and not nums[avg_i - 1] < target < nums[avg_i] \
            and not (nums[avg_i - 1] < target and target == nums[avg_i]):
            if nums[avg_i] >= target:
                max_i = avg_i
            else:
                min_i = avg_i
            avg_i = (min_i + max_i + 1) // 2
        if nums[avg_i] != target:
            return [-1, -1]
        result.append(avg_i)
        print(avg_i)
        min_i, max_i = avg_i, max_val
        # search for max index
        while avg_i < len(nums) - 1 and not (nums[avg_i + 1] > nums[avg_i] and nums[avg_i] == target):
            if nums[avg_i] <= target:
                min_i = avg_i
            else:
                max_i = avg_i
            avg_i = (min_i + max_i + 1) // 2
        result.append(avg_i)
        print(avg_i)
        return result
        
    
def main():
    sol = Solution()
    # test 1
    nums = [5,7,7,8,8,10]
    target = 8
    print(sol.searchRange(nums, target), 'should equal [3,4]')
    # test 2
    nums = [5,7,7,8,8,10]
    target = 6
    print(sol.searchRange(nums, target), 'should equal [-1,-1]')
    # test 3
    nums = []
    target = 0
    print(sol.searchRange(nums, target), 'should equal [-1,-1]')
    # test 4
    nums = [1, 2, 2]
    target = 2
    print(sol.searchRange(nums, target), 'should equal [1,2]')
    # test 5
    nums = [-3,-2,-1]
    target = 0
    print(sol.searchRange(nums, target), 'should equal [-1,-1]')


if __name__ == '__main__':
    main()
    
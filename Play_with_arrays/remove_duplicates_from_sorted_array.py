'''
my solution to task: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
'''


from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for i, val_1, val_2 in zip(range(len(nums) - 1, 0, -1), nums[-2::-1], nums[::-1]):
            if val_1 == val_2:
                del nums[i]
        return len(nums)
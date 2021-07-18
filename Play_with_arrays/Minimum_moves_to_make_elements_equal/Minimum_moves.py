class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums[0] == sorted_nums[-1]:
            return 0
        
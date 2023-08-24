'''

my solution to task: https://leetcode.com/problems/minimum-size-subarray-sum/

'''

from typing import List

# slower version

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        act_array, min_val = [], len(nums)
        for num in nums:
            act_array.append(num)
            while sum(act_array) >= target:
                if len(act_array) < min_val:
                    min_val = len(act_array)
                act_array = act_array[1:]
        return min_val

# faster version

class Solution2:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        min_val, cum_nums = len(nums), [nums[0]]
        for num in nums[1:]:
            cum_nums.append(cum_nums[-1] + num)
        print(cum_nums)
        return min_val
    

def main():
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]), 'should equal 2')
    print(sol.minSubArrayLen(4, [1,4,4]), 'should equal 1')
    print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 'should equal 0')
    print(sol.minSubArrayLen(11, [1,2,3,4,5]), 'should equal 3')
    sol = Solution2()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]), 'should equal 2')
    print(sol.minSubArrayLen(4, [1,4,4]), 'should equal 1')
    print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 'should equal 0')
    print(sol.minSubArrayLen(11, [1,2,3,4,5]), 'should equal 3')
    

if __name__ == '__main__':
    main()
    
        
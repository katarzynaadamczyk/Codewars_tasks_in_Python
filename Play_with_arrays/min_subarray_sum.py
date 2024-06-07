'''

my solution to task: https://leetcode.com/problems/minimum-size-subarray-sum/

'''

from typing import List

# solution with O(n) speed    
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if target > sum(nums):
            return 0
        min_len, start_k, act_sum = len(nums), 0, 0
        for i, val in enumerate(nums):
            act_sum += val
            changed = False
            while act_sum >= target and i >= start_k:
                act_sum -= nums[start_k]
                start_k += 1
                changed = True
            if changed:
                start_k -= 1
                act_sum += nums[start_k]
            if act_sum >= target and i - start_k + 1 < min_len:
                min_len = i - start_k + 1
        return min_len
    

def main():
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]), 'should equal 2')
    print(sol.minSubArrayLen(4, [1,4,4]), 'should equal 1')
    print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 'should equal 0')
    print(sol.minSubArrayLen(11, [1,2,3,4,5]), 'should equal 3')
    

if __name__ == '__main__':
    main()
    
        
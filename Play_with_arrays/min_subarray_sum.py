'''

my solution to task: https://leetcode.com/problems/minimum-size-subarray-sum/

'''

from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        act_array, min_val = [], len(nums) + 1
        for num in nums:
            act_array.append(num)
            print(act_array)
            while sum(act_array) > target:
                del act_array[0]
                print(act_array)
            if sum(act_array) == target and len(act_array) < min_val:
                min_val = len(act_array)
            print(act_array)
        return min_val if min_val <= len(nums) else 0
    
def main():
    sol = Solution()
    print(sol.minSubArrayLen(7, [2,3,1,2,4,3]), 'should equal 2')
    print(sol.minSubArrayLen(4, [1,4,4]), 'should equal 1')
    print(sol.minSubArrayLen(11, [1,1,1,1,1,1,1,1]), 'should equal 0')
    print(sol.minSubArrayLen(11, [1,2,3,4,5]), 'should equal 3')
    
    

if __name__ == '__main__':
    main()
    
        
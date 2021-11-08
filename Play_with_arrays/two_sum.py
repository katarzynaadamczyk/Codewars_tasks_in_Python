from typing import List

class Solution:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
                
class Solution_v2:
    @staticmethod
    def twoSum(nums: List[int], target: int) -> List[int]:
        dict = {}
        for i, num in enumerate(nums):
            if (target - num) in dict.keys():
                return [dict[target - num], i]
            dict[num] = i
        return [0, 0]
                

def main():
    print('First Solution:')
    print(f'For: [3,2,4] and target: 6 solution is {Solution.twoSum([3,2,4], 6)} (should be [1, 2])')
    print(f'For: [2,7,11,15] and target: 9 solution is {Solution.twoSum([2,7,11,15], 9)} (should be [0, 1])')
    print(f'For: [3,3] and target: 6 solution is {Solution.twoSum([3,3], 6)} (should be [0, 1])')
    print('Second Solution:')
    print(f'For: [3,2,4] and target: 6 solution is {Solution_v2.twoSum([3,2,4], 6)} (should be [1, 2])')
    print(f'For: [2,7,11,15] and target: 9 solution is {Solution_v2.twoSum([2,7,11,15], 9)} (should be [0, 1])')
    print(f'For: [3,3] and target: 6 solution is {Solution_v2.twoSum([3,3], 6)} (should be [0, 1])')
    

if __name__ == '__main__':
    main()
    
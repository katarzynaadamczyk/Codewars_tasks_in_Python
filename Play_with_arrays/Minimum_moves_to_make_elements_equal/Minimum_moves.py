from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)
        if sorted_nums[0] == sorted_nums[-1]:
            return 0
        
        median = sorted_nums[len(nums) // 2]
        result = 0

        for i in sorted_nums:
            result += abs(median - i)

        return result  

def main():
    sol = Solution()
    print(sol.minMoves2([1, 2, 3]))
    print(sol.minMoves2([5, 50, 25]))
    print(sol.minMoves2([60, 123, 58]))


if __name__ == '__main__':
    main()
    
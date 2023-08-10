''' my solution to taks found on LeetCode:  '''

from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ordered_nums, result = sorted(nums), []
        for index_1, num_1 in enumerate(ordered_nums[:-2]):
            if num_1 > 0:
                break
            for index_2, num_2 in enumerate(ordered_nums[index_1+1:-1]):
                if num_1 + num_2 > 0:
                    break
                num_3 = 0 - num_1 - num_2
                # check if num_3 is in nums
                max_index = len(ordered_nums) - 1
                min_index = min(index_1+index_2+2, max_index)
                mid_index = (min_index + max_index) // 2
                while True:
                    if ordered_nums[min_index] == num_3 or ordered_nums[max_index] == num_3 or ordered_nums[mid_index] == num_3:
                        if [num_1, num_2, num_3] not in result:
                            result.append([num_1, num_2, num_3])
                        break
                    if abs(max_index - min_index) <= 1:
                        break
                    if num_3 < ordered_nums[mid_index]:
                        max_index = mid_index
                    else:
                        min_index = mid_index
                    mid_index = (min_index + max_index) // 2
        return result
    
def main():
    sol = Solution()
    # test 1
    test_nums = [-1,0,1,2,-1,-4]
    print(sol.threeSum(test_nums), 'should equal [[-1, -1, 2], [-1, 0, 1]]')
    # test 2
    test_nums = [0,1,1]
    print(sol.threeSum(test_nums), 'should equal []')
    
    # test 3
    test_nums = [0,0,0]
    print(sol.threeSum(test_nums), 'should equal [[0, 0, 0]]')
    
if __name__ == '__main__':
    main()

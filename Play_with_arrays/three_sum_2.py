''' 

my solution to taks found on LeetCode:  

quicker solution

'''

from typing import List

class Solution:
    def three_generator(self):
        pass
    
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        self.sorted_unique_nums = sorted(list(set(nums)))
        self.nums_dict = {x: nums.count(x) for x in self.sorted_unique_nums}
        return [triple for triple in self.three_generator()]
    
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

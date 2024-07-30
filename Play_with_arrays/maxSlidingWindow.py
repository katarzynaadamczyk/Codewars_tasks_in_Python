'''
leetcode
239. Sliding Window Maximum
https://leetcode.com/problems/sliding-window-maximum/description/
learn how to use a deque


'''

from collections import deque
from typing import List

class Solution:
    # a deque solution
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        maxWindow = []
        slidingDeque = deque()
        for i, num in enumerate(nums):
            if i >= k and slidingDeque[0][1] == i - k:
                slidingDeque.popleft()
            while slidingDeque and slidingDeque[-1][0] <= num:
                slidingDeque.pop()
            slidingDeque.append((num, i))
            if i >= k - 1:
                maxWindow.append(slidingDeque[0][0])
        return maxWindow
    

    # brute force solution
    def maxSlidingWindow2(self, nums: List[int], k: int) -> List[int]:
        maxWindow = [max(nums[:k])]
        for i in range(k, len(nums)):
            if nums[i-k] >= maxWindow[-1]:
                maxWindow.append(max(nums[i-k+1:i+1]))
            else:
                maxWindow.append(max(maxWindow[-1], nums[i]))
        return maxWindow
        
def main():
    # tests
    sol = Solution()
    # test 1
    nums = [1,3,-1,-3,5,3,6,7]
    k = 3
    print(sol.maxSlidingWindow(nums, k), 'should equal [3, 3, 5, 5, 6, 7]')
    # test 2
    nums = [1]
    k = 1
    print(sol.maxSlidingWindow(nums, k), 'should equal [1]')
    # test 3
    with open('Play_with_arrays/Tests/maxSlidingWindow.txt', 'r') as myfile:
        nums = [int(x) for x in myfile.readline().strip().split(',')]
    k = 50000
    print(len(nums))
    #print(sol.maxSlidingWindow(nums, k), 'should equal ?')

if __name__ == '__main__':
    main()

'''
my solution to task:
https://leetcode.com/problems/kth-largest-element-in-an-array/

'''
from typing import List
from queue import PriorityQueue
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums_queue, lowest_num = PriorityQueue(), nums[0]
        for num in nums[:k]:
            nums_queue.put(num)
            lowest_num = min(lowest_num, num)
        for num in nums[k:]:
            val = nums_queue.get()
            nums_queue.put(val if val > num else num)
        return nums_queue.get()
    
    def findKthLargest2(self, nums: List[int], k: int) -> int:
        
        # heapify the input, in-place
        heapq.heapify(nums)

        # remove the topmost item from the heap
        # until k reached.
        while len(nums) > k:
            heapq.heappop(nums)
        return nums[0]






def main():
    sol = Solution()
    # test 1
    nums, k = [3,2,1,5,6,4], 2
    print(sol.findKthLargest2(nums, k), 'should equal 5')

    # test 2
    nums, k = [3,2,3,1,2,4,5,5,6], 4
    print(sol.findKthLargest2(nums, k), 'should equal 4')



if __name__ == '__main__':
    main()

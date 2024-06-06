'''
my solution to task : https://leetcode.com/problems/insert-interval/
'''

from typing import List        
import unittest


class Solution:
    @staticmethod
    def find_index(intervals: List[List[int]], value: int, min_index: int = 0) -> int:
        max_index, act_index = len(intervals), min_index
        intervals_len = max_index
        while act_index < intervals_len:
            if (act_index + 1 < intervals_len and intervals[act_index][0] <= value < intervals[act_index + 1][0]):
                return act_index
            elif act_index + 1 == intervals_len and intervals[act_index][0] <= value <= intervals[act_index][1]:
                return act_index

            act_index = (min_index + max_index + 1) // 2
            if intervals[act_index][0] < value:
                min_index = act_index
            else:
                max_index = act_index
        return act_index
            
        
        
        
    @staticmethod
    def insert(intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [[newInterval]]
        intervals.sort()
        if newInterval[0] < intervals[0][0]:
            min_index = -1
        else:
            min_index = Solution.find_index(intervals, newInterval[0])
        if min_index == len(intervals):
            intervals.append(newInterval)
            return intervals
        if min_index == -1 and newInterval[1] < intervals[0][0]:
            intervals.insert(0, newInterval)
            return intervals
        max_index = Solution.find_index(intervals, newInterval[1], max(min_index, 0))
        # jezeli oba sa takie same to co
        # jezeli max index jest poza lista
        # jezeli min index jest poza lista
        
        if max_index == len(intervals):
            pass
        # pozostale po prostu zrobic insert

class TestInsertInterval(unittest.TestCase):

    def test_simple_insertion(self):
        intervals = [[1,3],[6,9]]
        newInterval = [2,5]
        self.assertEqual(Solution.insert(intervals, newInterval), [[1,5],[6,9]])

    def test_interval_overlaps(self):
        intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
        newInterval = [4,8]
        self.assertEqual(Solution.insert(intervals, newInterval), [[1,2],[3,10],[12,16]])

if __name__ == '__main__':
    unittest.main()
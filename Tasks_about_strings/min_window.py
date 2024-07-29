'''
leetcode
task: 76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/description/
'''

from collections import Counter

class Solution:
    def findMinMaxIndex(self, s: str, tCounter: Counter) -> tuple[int, int]:
        minIndex, maxIndex = len(s) - 1, 0
        for char in tCounter.keys():
            minIndex = min(s.index(char), minIndex)
            maxIndex = max(s.rindex(char), maxIndex)
        return (minIndex, maxIndex)

    def checkCounters(self, sCounter: Counter, tCounter: Counter) -> bool:
        for char, value in tCounter.items():
            if sCounter[char] < value:
                return False
        return True
    
    def moveCounter(self, s: str, minIndex: int, maxIndex: int, tLength: int, tCounter: Counter) -> str:
        windows = set()
        if maxIndex - minIndex >= tLength and self.checkCounters(Counter(s[minIndex + 1:maxIndex + 1]), tCounter):
            windows.add(self.moveCounter(s, minIndex + 1, maxIndex, tLength, tCounter))
        if maxIndex - minIndex >= tLength and self.checkCounters(Counter(s[minIndex: maxIndex]), tCounter):
            windows.add(self.moveCounter(s, minIndex, maxIndex - 1, tLength, tCounter))
        if len(windows) == 0:
            return s[minIndex:maxIndex+1]
        return min(windows, key=lambda x: len(x))


    def minWindow(self, s: str, t: str) -> str:
        tCounter = Counter(t)
        if s == '' or not self.checkCounters(Counter(s), tCounter):
            return ''
        minIndex, maxIndex = self.findMinMaxIndex(s, tCounter)
        tLength = len(t)
        return self.moveCounter(s, minIndex, maxIndex, tLength, tCounter)

def main():
    sol = Solution()
    # test 1
    s = "ADOBECODEBANC"
    t = "ABC"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'BANC\'')
    # test 2
    s = "a"
    t = "a"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'a\'')
    # test 3
    s = ""
    t = "a"
    print('\'' + sol.minWindow(s, t) + '\'', 'should equal \'\'')

if __name__ == '__main__':
    main()
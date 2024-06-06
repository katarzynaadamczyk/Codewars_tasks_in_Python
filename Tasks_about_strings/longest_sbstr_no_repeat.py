'''
my solution to :

'''

from typing import List

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        num_of_chars, max_len = len(set(s)), 0
        for x in range(num_of_chars, max_len, -1):
            for i in range(len(s) - x + 1):
                if x == len(set(s[i:i+x])):
                    max_len = x
                    break
            if max_len > 0:
                break
        return max_len



'''
my solution to problem on LeetCode: https://leetcode.com/problems/is-subsequence/
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, found_letters = 0, ''
        for s_char in s:
            for index, t_char in enumerate(t[i:]):
                if s_char == t_char:
                    i += index + 1
                    found_letters += t_char
                    break
        return True if len(found_letters) == len(s) else False
    
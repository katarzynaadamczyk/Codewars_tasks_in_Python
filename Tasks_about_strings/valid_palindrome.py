''' my solution to task on LeetCode : https://leetcode.com/problems/valid-palindrome/ '''

class Solution:
    acceptable = 'abcdefghijklmnopqrstuwvxyz0123456789'
    def isPalindrome(self, s: str) -> bool:
        s, new_s = s.lower(), ''
        for char in s:
            if char in Solution.acceptable:
                new_s += char
        for char_1, char_2 in zip(new_s, new_s[::-1]):
            if char_1 != char_2:
                return False
        return True

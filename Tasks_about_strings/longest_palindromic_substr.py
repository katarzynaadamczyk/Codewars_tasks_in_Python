'''
leetcode
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

'''

from queue import Queue

class Solution:
    def getActualLongestPalindrome(self, s: str, iMin: int, iMax: int, n: int) -> str:
        if iMin < 0 or iMax > n:
            return ''
        while s[iMin:iMax+1] == s[iMin:iMax+1][::-1]:
                if iMin > 0 and iMax < n - 1:
                    iMin -= 1
                    iMax += 1
                else:
                    break
        return s[iMin:iMax+1] if s[iMin:iMax+1] == s[iMin:iMax+1][::-1] else s[iMin + 1:iMax]
    
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n < 2:
            return s
        if s == s[::-1]:
            return s
        longestPalindrome, maxLen = s[0], 1
        indexQueue = Queue()
        indexQueue.put(n // 2)
        checkedIndexes = set()
        checkedIndexes.add(n // 2)
        while not indexQueue.empty():
            # get actual index to check
            actIndex = indexQueue.get()
            # put next indexes to queue
            if actIndex - 1 >= 0 and actIndex - 1 not in checkedIndexes:
                indexQueue.put(actIndex - 1)
                checkedIndexes.add(actIndex - 1)
            if actIndex + 1 < n and actIndex + 1 not in checkedIndexes:
                indexQueue.put(actIndex + 1)
                checkedIndexes.add(actIndex + 1)
            # check palindromes around actual index
            for iMin, iMax in [(actIndex, actIndex + 1), (actIndex - 1, actIndex), (actIndex - 1, actIndex + 1)]:
                newPalindrome = self.getActualLongestPalindrome(s, iMin, iMax, n)
                if len(newPalindrome) > maxLen:
                    maxLen = len(newPalindrome)
                    longestPalindrome = newPalindrome

        return longestPalindrome
    
def main():
    # tests
    sol = Solution()
    # test 1
    s = "babad"
    print(sol.longestPalindrome(s), 'should equal \'aba\' or \'bab\'')
    # test 2
    s = "caba"
    print(sol.longestPalindrome(s), 'should equal \'aba\'')

if __name__ == '__main__':
    main()

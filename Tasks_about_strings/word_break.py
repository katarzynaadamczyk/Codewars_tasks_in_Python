'''
my solution to task from leetcode:
https://leetcode.com/problems/word-break/

'''
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # defining starting needed variables
        len_s = len(s)
        # changing wordDict to set -> quickest check if word exist in it
        wordDict = set(wordDict)
        # preparing dp table
        dp = [False] * (len_s + 1)
        # first element need to be true as it represents an empty string
        dp[0] = True 
        # fill in dp table:
        for i in range(len_s + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[-1]


def main():
    sol = Solution()
    # test 1
    s = 'catsandog'
    wordDict = ['cats', 'dog', 'sand', 'and', 'cat']
    print(sol.wordBreak(s, wordDict), 'should equal False')
    
    
    # test 2
    s = 'applepenapple'
    wordDict = ['apple', 'pen']
    print(sol.wordBreak(s, wordDict), 'should equal True')


    # test 3
    s = 'leetcode'
    wordDict = ['leet', 'code']
    print(sol.wordBreak(s, wordDict), 'should equal True')


if __name__ == '__main__':
    main()
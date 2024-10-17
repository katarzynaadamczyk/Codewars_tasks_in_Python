'''
my solution to task from leetcode:
https://leetcode.com/problems/edit-distance/

'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # beginning conditions
        if word1 == '':
            return len(word2)
        if word2 == '':
            return len(word1)
        len1, len2 = len(word1), len(word2)
        # prepare dp table
        dp = []
        for i in range(len1 + 1):
            dp.append([i])
        for j in range(1, len2 + 1):
            dp[0].append(j)
        # fill in dp table
        for i in range(1, len1 + 1):
            for j in range(1, len2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i].append(dp[i-1][j-1])
                else:
                    dp[i].append(min(dp[i-1][j-1], dp[i-1][j], dp[i][-1]) + 1)
        return dp[-1][-1]


def main():
    sol = Solution()
    # test 1
    word1, word2 = '', ''
    print(sol.minDistance(word1, word2), 'should equal 0')
    
    
    # test 2
    word1, word2 = 'horse', 'ros'
    print(sol.minDistance(word1, word2), 'should equal 3')


    # test 3
    word1, word2 = 'intention', 'execution'
    print(sol.minDistance(word1, word2), 'should equal 5')

    # test 4
    word1, word2 = 'a', 'aaa'
    print(sol.minDistance(word1, word2), 'should equal 2')


if __name__ == '__main__':
    main()
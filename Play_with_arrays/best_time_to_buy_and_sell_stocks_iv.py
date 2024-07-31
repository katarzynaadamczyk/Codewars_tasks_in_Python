'''
leetcode
188. Best Time to Buy and Sell Stock IV
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/


'''

from typing import List

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        buy = [1000] * k
        sell = [0] * k
        for price in prices:
            buy[0] = min(buy[0], price)
            sell[0] = max(sell[0], price - buy[0])
            for j in range(1, k):
                buy[j] = min(buy[j], price - sell[j-1])
                sell[j] = max(sell[j], price - buy[j])

        return sell[-1]

def main():
    sol = Solution()
    # test 1
    prices = [2,4,1]
    k = 2
    print(sol.maxProfit(k, prices), 'should equal 2')
    
    
    # test 2
    prices = [3,2,6,5,0,3]
    k = 2
    print(sol.maxProfit(k, prices), 'should equal 7')
    

if __name__ == '__main__':
    main()
    
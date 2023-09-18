'''
my solution to task: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
'''

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        act_min, profit, profits = prices[0], 0, []
        for val in prices[1:]:
            if val < act_min:
                act_min = val
            elif profit < val - act_min:
                profit = val - act_min
        return profit
        
def main():
    pass

if __name__ == '__main__':
    main()
    
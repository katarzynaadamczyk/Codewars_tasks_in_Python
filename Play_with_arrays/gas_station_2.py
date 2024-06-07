'''
my solution to task: https://leetcode.com/problems/gas-station/
using Kadane's algorithm 

'''

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost) or sum(gas) <= 0:
            return -1
        self.n = len(gas)
        if self.n == 1:
            return 0
        # prepare list gas[i] - cost[i]
        self.gas_minus_cost = [g - c for g, c in zip(gas, cost)]
        # look for starting index to search for max subarray sum
       # k = 0 # first non-minus value index
        # decide if move clockwise or counterclockwise
      #  if self.gas_minus_cost[0] >= 0:
            # search counterclockwise
      #      while self.gas_minus_cost[k] >= 0 and (k - 1) % self.n != 0:
       #         k -= 1
       #     k = k % self.n
        # find max subarray sum and its starting index
        max_index, act_max_index = 0, 0
        max_ending_here = 0
        max_so_far = min(self.gas_minus_cost)
        
     #   print(self.n, k)
        for i in range(2 * self.n):
            max_ending_here += self.gas_minus_cost[i % self.n]
            if max_ending_here < 0:
                act_max_index = i + 1
                max_ending_here = 0
            elif max_ending_here > max_so_far:
                max_index = act_max_index
                max_so_far = max_ending_here
        if max_so_far > 0:
            return max_index % self.n
        




        return -1


# tests
def main():
    sol = Solution()
    # test 1
    gas = [1,2,3,4,5] 
    cost = [3,4,5,1,2]
    print(sol.canCompleteCircuit(gas, cost), 'should equal 3')
    # test 2
    gas = [2,3,4]
    cost = [3,4,3]
    print(sol.canCompleteCircuit(gas, cost), 'should equal -1')
    # test 3
    with open('play_with_arrays/tests/gas.txt') as myfile:
        line = myfile.readline()
        line = line.strip().strip('[]')
    gas = [int(x) for x in line.split(',')]
    with open('play_with_arrays/tests/costs.txt') as myfile:
        line = myfile.readline()
        line = line.strip().strip('[]')
    cost = [int(x) for x in line.split(',')]
    print(sol.canCompleteCircuit(gas, cost), 'should equal 99999')
    # test 4
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    print(sol.canCompleteCircuit(gas, cost), 'should equal 4')
    # test 5
    gas = [7,1,0,11,4]
    cost = [5,9,1,2,5]
    print(sol.canCompleteCircuit(gas, cost), 'should equal 3')
    
    # test 6
    with open('play_with_arrays/tests/gas2.txt') as myfile:
        line = myfile.readline()
        line = line.strip().strip('[]')
    gas = [int(x) for x in line.split(',')]
    with open('play_with_arrays/tests/costs2.txt') as myfile:
        line = myfile.readline()
        line = line.strip().strip('[]')
    cost = [int(x) for x in line.split(',')]
    print(sol.canCompleteCircuit(gas, cost), 'should equal 0')
    # test 7
    gas = [5,8,2,8]
    cost = [6,5,6,6]
    print(sol.canCompleteCircuit(gas, cost), 'should equal 3')


if __name__ == '__main__':
    main()
'''
my solution to task: https://leetcode.com/problems/gas-station/


'''

from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost) or sum(gas) <= 0:
            return -1
        self.n = len(gas)
        # prepare list gas[i] - cost[i]
        self.gas_minus_cost = [g - c for g, c in zip(gas, cost)]
        # find first non-minus value 
        k = 0 # first non-minus value index
        # decide if move clockwise or counterclockwise
        if self.gas_minus_cost[0] >= 0:
            # search counterclockwise
            while self.gas_minus_cost[k] >= 0 and (k - 1) % self.n != 0:
                k -= 1
            k = (k + 1) % self.n
        else:
            # search clockwise
            k = 0
            while self.gas_minus_cost[k] < 0 and (k + 1) % self.n != 0:
                k += 1
       # print(self.gas_minus_cost)
        print(k)
        # generate a 'circle'
        k_w = k
        section_dict = {}
        while k + self.n != k_w:
            new_k_w = self.findSection(k_w)
            if new_k_w > self.n:
                act_val = sum(self.gas_minus_cost[k_w % self.n:]) + sum(self.gas_minus_cost[:new_k_w % self.n])
            else:
                act_val = sum(self.gas_minus_cost[k_w % self.n:new_k_w])
            section_dict[k_w % self.n] = act_val
            k_w = new_k_w
            print(k_w)
        print(section_dict)
        # check on circle
        lst_of_indexes = list(section_dict.keys())
        lst_of_vals = list(section_dict.values())
        for i, index in enumerate(lst_of_indexes):
            act_val = 0
            for val in (lst_of_vals[i:] + lst_of_vals[:i]):
                act_val += val
                if act_val < 0:
                    break
            if act_val >= 0:
                return index

        return -1
    

    # function to find first negative value after k_w index
    def findFirstMinus(self, k_w: int) -> int:
        while self.gas_minus_cost[k_w % self.n] >= 0:
            k_w += 1
        return k_w

    # function to find first positive value after k_w index
    def findFirstPlus(self, k_w: int) -> int:
        while self.gas_minus_cost[k_w % self.n] < 0:
            k_w += 1
        return k_w
    
    # function to find whole section up and down
    def findSection(self, k_w: int) -> int:
        return self.findFirstPlus(self.findFirstMinus(k_w))

# tests
def main():
    sol = Solution()
    '''
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
    print(sol.canCompleteCircuit(gas, cost), 'should equal ?')
    # test 4
    gas = [5,1,2,3,4]
    cost = [4,4,1,5,1]
    print(sol.canCompleteCircuit(gas, cost), 'should equal 4')
    # test 5
    gas = [7,1,0,11,4]
    cost = [5,9,1,2,5]
    print(sol.canCompleteCircuit(gas, cost), 'should equal 3')
    
   '''
    # test 6
    with open('play_with_arrays/tests/gas2.txt') as myfile:
        line = myfile.readline()
        line = line.strip().strip('[]')
    gas = [int(x) for x in line.split(',')]
    with open('play_with_arrays/tests/costs2.txt') as myfile:
        line = myfile.readline()
        line = line.strip().strip('[]')
    cost = [int(x) for x in line.split(',')]
    print(sol.canCompleteCircuit(gas, cost), 'should equal ?')
    print(sol.n, sol.gas_minus_cost.count(0), gas.count(0))

if __name__ == '__main__':
    main()
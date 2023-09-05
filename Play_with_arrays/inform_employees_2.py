'''
my solution to task : https://leetcode.com/problems/time-needed-to-inform-all-employees/
'''

from typing import Dict, List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.uniqueManagers = set(manager)
        self.uniqueManagers.remove(manager[headID])
        self.managers = self.getDictManagers(manager)
        del self.managers[manager[headID]]
        self.times = {}
        self.informTime = informTime
        return self.getTime(headID)
    
    def getDictManagers(self, managers: List[int]):
        managerEmployeeDict = {}
        for index, value in enumerate(managers):
            managerEmployeeDict.setdefault(value, [])
            managerEmployeeDict[value].append(index)
        return managerEmployeeDict
    
    def getTime(self, employee: int) -> int:
        if employee not in self.uniqueManagers:
            return self.informTime[employee]
        if employee not in self.times.keys():
            self.times[employee] = self.informTime[employee] + max([self.getTime(worker) for worker in self.managers[employee]])
        return self.times[employee]

def main():
    tester = Solution()
    
    # test 1
    informTime = [0]
    manager = [-1]
    headId = 0
    n = 1
    print(tester.numOfMinutes(n, headId, manager, informTime), 'should equal 0')
    
    # test 2
    informTime = [0,0,1,0,0,0]
    manager = [2,2,-1,2,2,2]
    headId = 2
    n = 6
    print(tester.numOfMinutes(n, headId, manager, informTime), 'should equal 1')
    
    # test 3
    informTime = [1,1,1,1,1,1,1,0,0,0,0,0,0,0,0]
    manager = [-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
    headId = 0
    n = 15
    print(tester.numOfMinutes(n, headId, manager, informTime), 'should equal 3')
    
    
    
if __name__ == '__main__':
    main()




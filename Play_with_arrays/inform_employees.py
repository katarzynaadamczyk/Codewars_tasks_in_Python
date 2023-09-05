'''
my solution to task : https://leetcode.com/problems/time-needed-to-inform-all-employees/
'''

from typing import Dict, List, Optional, Set, Type

class Node:
    maxIndex = 0
    maxtime = 0
    
    def __init__(self, n: int, index: int, uniqueManagers: Set[int], managers: Dict[int, List[int]], informTime: List[int], previous = None) -> None:
        self.index = index
        if previous is None:
            Node.maxtime = 0
        Node.maxIndex = n - 1
        self.next = managers.get(self.index, [])
        self.previous = previous
        self.time = self.previous.getTime() + informTime[self.previous.getIndex()] if self.previous else 0
        Node.maxtime = self.time if self.time > Node.maxtime else Node.maxtime
        self.nextNodes = []
        for index in self.next:
            self.nextNodes.append(Node(n, index, uniqueManagers, managers, informTime, self))
    
    def getTime(self) -> int:
        return self.time
    
    def getIndex(self) -> int:
        return self.index

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        uniqueManagers = set(manager)
        managers = self.getDictManagers(manager)
        root = Node(n, headID, uniqueManagers, managers, informTime)
        return Node.maxtime
    
    def getDictManagers(self, managers: List[int]):
        managerEmployeeDict = {}
        for index, value in enumerate(managers):
            managerEmployeeDict.setdefault(value, [])
            managerEmployeeDict[value].append(index)
        return managerEmployeeDict

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




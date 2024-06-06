'''
my solution to:
https://leetcode.com/problems/happy-number/

'''

from typing import List

class Solution:
    def isHappy(self, n: int) -> bool:
        numbers = set()
        while n not in numbers:
            numbers.add(n)
            n = sum(list(map(lambda x: x ** 2, [int(char) for char in str(n)])))
            if n == 1:
                return True
        return False
    
def main():
    # tests 
    
    sol = Solution()
    
    # test 1
    print(sol.isHappy(19), 'should equal True')
    
    # test 2
    print(sol.isHappy(2), 'should equal False')
    
if __name__ == '__main__':
    main()
    
    
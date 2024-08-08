'''
my solution to problem:
https://leetcode.com/problems/valid-parentheses/

'''


class Solution:
    
    brackets = {'(': ')', '[': ']', '{': '}'}
    
    def isValid(self, s: str) -> bool:
        stack = ''
        for char in s:
            if char in Solution.brackets.keys():
                stack += Solution.brackets[char]
            elif len(stack) and stack[-1] == char:
                stack = stack[:-1]
            else:
                return False
        return True if len(stack) == 0 else False
    
def main():
    # test
    sol = Solution()
    
    # test 1
    print(sol.isValid('((()))'), 'should equal True')
    
    # test 2 
    print(sol.isValid('((('), 'should equal False')

if __name__ == '__main__':
    main()

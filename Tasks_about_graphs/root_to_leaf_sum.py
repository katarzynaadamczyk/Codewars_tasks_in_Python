from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    @staticmethod
    def rek(num, node, count):
        if node.right is None and node.left is None:
            return num // 10, node, count + num * 10 + node.val
        if node.right is not None:
            num, node2, count = Solution.rek(num * 10 + node.val, node.right, count)
        if node.left is not None:
            num, node2, count = Solution.rek(num * 10 + node.val, node.left, count)
        return num // 10, node, count

    @staticmethod
    def sumNumbers(root: Optional[TreeNode]) -> int:
        num, node2, count = Solution.rek(0, root, 0)
        return count


class Solution_v2:
    @staticmethod
    def sumNumbers(root: Optional[TreeNode]) -> int:
        def rek(root, sum):
            if not root:
                return 0
            if not root.left and not root.right:
                return int(sum + str(root.val))
            return rek(root.right, sum + str(root.val)) + rek(root.left, sum + str(root.val))
        return rek(root, '')
    
class Solution_v3:
    @staticmethod
    def sumNumbers(root: Optional[TreeNode]) -> int:
        def rek(root: Optional[TreeNode], sum: str) -> str:
            if not root:
                return 0
            if not root.left and not root.right:
                return sum + str(root.val)
            return int(rek(root.right, sum + str(root.val))) + int(rek(root.left, sum + str(root.val)))
        return rek(root, '')


def main():
    three = TreeNode(3)
    two = TreeNode(2)
    one = TreeNode(1, three, two)
    print(Solution.sumNumbers(one))
    print(Solution_v2.sumNumbers(one))
    print(Solution_v3.sumNumbers(one))
    

if __name__ == '__main__':
    main()
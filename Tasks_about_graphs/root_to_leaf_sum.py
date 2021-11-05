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
        print(f'num: {num}')
        print(f'count: {count}')
        print(f'node.val: {node.val}')
        if node.right is None and node.left is None:
            return num, node, count + num * 10 + node.val
        if node.right is not None:
            num, node2, count = Solution.rek(num * 10 + node.val, node.right, count)
        if node.left is not None:
            num, node2, count = Solution.rek(num, node.left, count)
        return num // 10, node, count

    @staticmethod
    def sumNumbers(root: Optional[TreeNode]) -> int:
        num, node2, count = Solution.rek(0, root, 0)
        return count




def main():
    three = TreeNode(3)
    two = TreeNode(2)
    one = TreeNode(1, three)
    print(Solution.sumNumbers(one))
    pass
    

if __name__ == '__main__':
    main()
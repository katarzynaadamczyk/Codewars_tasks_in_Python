''' exercise binary search tree '''

class TreeNode:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return f'TreeNode(data={self.data}, left={self.left}, right={self.right})'


class BinarySearchTree:
    def __init__(self, tree_data):
        self.root = None
        if tree_data:
            self.root = TreeNode(tree_data[0])
        for value in tree_data[1:]:
            new_leaf = TreeNode(value)
            leaf = self.root
            while True:
                if leaf.data < value and leaf.right is None:
                    leaf.right = new_leaf
                    break
                if leaf.data >= value and leaf.left is None:
                    leaf.left = new_leaf
                    break
                leaf = leaf.right if leaf.data < value else leaf.left

    def data(self):
        return self.root

    def sorted_data(self):
        pass

def main():
    pass

if __name__ == '__main__':
    main()
    
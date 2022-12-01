''' exercise custom set '''
'''
keep set as binary search tree
'''


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
                if leaf.data == value:
                    break
                if leaf.data < value and leaf.right is None:
                    leaf.right = new_leaf
                    break
                if leaf.data > value and leaf.left is None:
                    leaf.left = new_leaf
                    break
                leaf = leaf.right if leaf.data < value else leaf.left

    def data(self):
        return self.root

    def sorted_data(self):
        return self.get_sorted_data(self.root)
    
    def get_sorted_data(self, leaf):
        if leaf is None:
            return []
        left = [] if leaf.left is None else self.get_sorted_data(leaf.left)
        right = [] if leaf.right is None else self.get_sorted_data(leaf.right)
        return left + [leaf.data] + right

    def __contains__(self, element):
        leaf = self.root
        while leaf is not None:
            if element > leaf.data:
                leaf = leaf.right
            elif element < leaf.data:
                leaf = leaf.left
            elif element == leaf.data:
                return True
        return False

class CustomSet:
    def __init__(self, elements=[]):
        self.set_tree = BinarySearchTree(elements)

    def isempty(self):
        return self.set_tree.data() is None

    def __contains__(self, element):
        return element in self.set_tree

    def issubset(self, other):
        my_elements = self.set_tree.sorted_data()
        for elem in my_elements:
            if elem not in other.set_tree:
                print(elem)
                return False
        return True

    def isdisjoint(self, other):
        other_elements = other.set_tree.sorted_data()
        for elem in other_elements:
            if elem in self.set_tree:
                return False
        return True

    def __eq__(self, other):
        return other.set_tree.sorted_data() == self.set_tree.sorted_data()

    def add(self, element):
        pass

    def intersection(self, other):
        pass

    def __sub__(self, other):
        pass

    def __add__(self, other):
        pass
    
    def __repr__(self) -> str:
        return str(self.set_tree.sorted_data())

def main():
    set1 = CustomSet([1, 2, 3])
    set2 = CustomSet([1, 2, 3])
    print(set1.issubset(set2))

if __name__ == '__main__':
    main()

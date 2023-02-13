''' exercise zipper '''


class Zipper:
    
    def __init__(self, data, parent) -> None:
        self.parent = parent
        self.set_value(data.get('value', 0))
        self.set_left(data.get('left', None))
        self.set_right(data.get('right', None))
    
    @staticmethod
    def from_tree(tree):
        root = Zipper(tree, None)
        return root

    def value(self):
        return self.value

    def set_value(self, number):
        self.value = number

    def left(self):
        return self.left

    def set_left(self, data):
        if data is not None:
            self.left = Zipper(data, self)
        else:
            self.left = None

    def right(self):
        self.right

    def set_right(self, data):
        if data is not None:
            self.right = Zipper(data, self)
        else:
            self.right = None

    def up(self):
        pass

    def to_tree(self):
        pass

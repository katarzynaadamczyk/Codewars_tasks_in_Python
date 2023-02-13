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
        return self.__value__

    def set_value(self, number):
        self.__value__ = number

    def left(self):
        return self.__left__

    def set_left(self, data):
        if data is not None:
            self.__left__ = Zipper(data, self)
        else:
            self.__left__ = None

    def right(self):
        self.__right__

    def set_right(self, data):
        if data is not None:
            self.__right__ = Zipper(data, self)
        else:
            self.__right__ = None

    def up(self):
        return self.parent

    def to_tree(self):
        self_tree = dict()
        self_tree.setdefault('value', self.value())
        if self.__left__ is None:
            self_tree.setdefault('left', None)
        else:
            self_tree.setdefault('left', self.__left__.to_tree())
        if self.__right__ is None:
            self_tree.setdefault('right', None)
        else:
            self_tree.setdefault('right', self.__right__.to_tree())
        return self_tree


def main():
    initial = {
    "value": 1,
    "left": {
        "value": 2,
        "left": None,
        "right": {"value": 3, "left": None, "right": None},
    },
    "right": {"value": 4, "left": None, "right": None},
    }

    zipper = Zipper.from_tree(initial)
    print(zipper.left())
    print(zipper.left().right())
    result = zipper.left().right().value()
    print(result)
    
if __name__ == '__main__':
    main()
    
    
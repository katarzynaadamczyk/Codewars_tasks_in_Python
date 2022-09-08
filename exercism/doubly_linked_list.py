''' exercise linked list  '''

class Node:
    def __init__(self, value, succeeding=None, previous=None):
        self.__value__ = value
        self.__next__ = succeeding
        self.__previous__ = previous

    def value(self):
        return self.__value__

    def next(self):
        return self.__next__
        
    def previous(self):
        return self.__previous__

    def set_next(self, next=None):
        self.__next__ = next

    def set_previous(self, previous=None):
        self.__previous__ = previous


class LinkedList:
    def __init__(self, vals=[]):
        self.__head__ = None
        self.__tail__ = None
        for val in vals:
            self.push(val)

    def push(self, value):
        newNode = Node(value, None, self.__head__)
        if self.__tail__ is None:
            self.__tail__ = newNode
        if self.__head__ is not None:
            self.__head__.set_next(newNode)
        self.__head__ = newNode
        return value

    def pop(self):
        retVal = self.__head__.value()
        self.__head__ = self.__head__.previous()
        return retVal

    def shift(self):
        retVal = self.__tail__.value()
        self.__tail__ = self.__tail__.next()
        return retVal

    def unshift(self, value):
        newNode = Node(value, self.__tail__, None)
        if self.__head__ is None:
            self.__head__ = newNode
        if self.__tail__ is not None:
            self.__tail__.set_previous(newNode)
        self.__tail__ = newNode
        return value

def tests():
    lst = LinkedList()
    lst.push(10)
    lst.push(20)
    print(lst.shift(), 'should be: ', 10)
    print(lst.shift(), 'should be: ', 20)
    
if __name__ == '__main__':
    tests()
    
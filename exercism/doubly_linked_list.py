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
    def __init__(self):
        pass

    def push(self, value):
        pass

    def pop(self):
        pass

    def shift(self):
        pass

    def unshift(self, value):
        pass

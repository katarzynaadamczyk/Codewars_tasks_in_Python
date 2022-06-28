''' exercise linked list FIFO '''

class Node:
    def __init__(self, value):
        self.__value__ = value
        self.__next__ = None

    def value(self):
        return self.__value__

    def next(self):
        return self.__next__

    def set_next(self, next):
        self.__next__ = next


class LinkedList:
    def __init__(self, values=[]):
        self.__head__ = None
        self.__length__ = 0
        for value in values:
            self.push(value)

    def __len__(self):
        return self.__length__

    def head(self):
        if self.__head__ is None:
            raise EmptyListException('The list is empty.')
        return self.__head__

    def push(self, value):
        new_node = Node(value)
        new_node.set_next(self.__head__)
        self.__head__ = new_node
        self.__length__ += 1

    def pop(self):
        if self.__head__ is None:
            raise EmptyListException('The list is empty.') 
        value = self.__head__.value()
        self.__head__ = self.__head__.next()
        self.__length__ -= 1
        return value

    def reversed(self):
        new_list = LinkedList()
        for elem in self:
            new_list.push(elem)
        return new_list

    def __iter__(self):
        self.act_iter_obj = self.__head__
        return self

    def __next__(self):
        if self.act_iter_obj is None:
            raise StopIteration
        act_value = self.act_iter_obj.value()
        self.act_iter_obj = self.act_iter_obj.next()
        return act_value

    def __repr__(self):
        text_repr = ''
        for elem in self:
            if text_repr != '':
                text_repr += ' <- '
            text_repr += str(elem)
        return text_repr


class EmptyListException(Exception):
    def __init__(self, message):
        self.message = message
        

if __name__ == '__main__':
    lst = LinkedList([1,2,3])
    print(lst)
    lst.pop()
    print(len(lst))
    print(lst)
    lst.push(4)
    lst.push(7)
    print(len(lst))
    print(lst)
    
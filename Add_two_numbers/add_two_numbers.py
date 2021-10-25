from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    @staticmethod
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # TODO
        pass

def add_node(num, next=None, lst=[]):
    node = ListNode(num, next=next)
    lst.append(node)
    return lst


def main():
    lst = add_node(3)
    lst = add_node(4, lst[0], lst)
    lst = add_node(4, lst[1], lst)
    print(lst)
    pass


if __name__ == '__main__':
    main()
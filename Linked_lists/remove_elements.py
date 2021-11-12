from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    @staticmethod
    def removeElements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
        def removeHead(head: ListNode):
            head2 = head.next
            del head
            return head2

        

def main():
    pass
    

if __name__ == '__main__':
    main()
    
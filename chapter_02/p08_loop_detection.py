from linked_list import LinkedList
from LL import MyLL
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    
    def detectLoop(self,head):
        '''returns Node where fast and slow pointer meet indicating the linked list has a cycle in it else returns None'''
        slow=fast=head
        if fast==None or fast.next==None or fast.next.next==None:
            return None
        fast=fast.next.next
        while (fast.next!=None and fast.next.next!=None) and (slow!=fast):
            slow=slow.next
            fast=fast.next.next
        if fast.next==None or fast.next.next==None:
            return None
        return fast
        
    
    def getCount(self,startNode):
        '''finds number of nodes in the cycle of a linked list'''
        slow=fast=startNode
        slow=slow.next
        fast=fast.next.next
        count=1
        while fast!=slow:
            slow=slow.next
            fast=fast.next.next
            count+=1
        return count
    
    def findBeginning(self,head,loopSize):
        '''finds the beginning node of a cycle in a linked list'''
        left=right=head
        for _ in range(loopSize-1):
            right=right.next
        while right.next!=left:
            left=left.next
            right=right.next
        return left
        
    def detectCycle(self, head: ListNode) -> ListNode:
        '''does as asked in question'''
        startNode=self.detectLoop(head)
        if startNode==None:
            return None
        loopSize=self.getCount(startNode)
        loopStart=self.findBeginning(head,loopSize)
        return loopStart

def loop_detection(ll):
    fast = slow = ll.head

    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast is slow:
            break

    if fast is None or fast.next is None:
        return None

    slow = ll.head
    while fast is not slow:
        fast = fast.next
        slow = slow.next

    return fast


def test_loop_detection():
    looped_list = LinkedList(["A", "B", "C", "D", "E"])
    loop_start_node = looped_list.head.next.next
    looped_list.tail.next = loop_start_node
    tests = [
        (LinkedList(), None),
        ((LinkedList((1, 2, 3))), None),
        (looped_list, loop_start_node),
    ]

    for ll, expected in tests:
        assert loop_detection(ll) == expected

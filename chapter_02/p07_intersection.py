from linked_list import LinkedList
from LL import MyLL

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        size1=1
        size2=1
        curr1=headA
        curr2=headB
        if curr1==None or curr2==None:
            return None
        while curr1.next!=None:
            curr1=curr1.next
            size1+=1
        while curr2.next!=None:
            curr2=curr2.next
            size2+=1
        if curr1!=curr2:
            return None
        if(size1>=size2):
            larger=headA
            smaller=headB
        else:
            larger=headB
            smaller=headA
        for _ in range(abs(size1-size2)):
            larger=larger.next
        while larger!=None:
            if larger==smaller:
                return larger
            larger=larger.next
            smaller=smaller.next
        return None
            

def intersection(list1, list2):
    if list1.tail is not list2.tail:
        return False

    shorter = list1 if len(list1) < len(list2) else list2
    longer = list2 if len(list1) < len(list2) else list1

    diff = len(longer) - len(shorter)

    shorter_node, longer_node = shorter.head, longer.head

    for _ in range(diff):
        longer_node = longer_node.next

    while shorter_node is not longer_node:
        shorter_node = shorter_node.next
        longer_node = longer_node.next

    return longer_node


def test_linked_list_intersection():
    shared = LinkedList()
    shared.add_multiple([1, 2, 3, 4])

    a = LinkedList([10, 11, 12, 13, 14, 15])
    b = LinkedList([20, 21, 22])

    a.tail.next = shared.head
    a.tail = shared.tail
    b.tail.next = shared.head
    b.tail = shared.tail

    # should be 1
    assert intersection(a, b).value == 1

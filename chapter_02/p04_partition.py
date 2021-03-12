from linked_list import LinkedList
from LL import MyLL
from LL import Node

def getLen(head):
    curr=head
    ctr=0
    while curr!=None:
        curr=curr.nxt 
        ctr+=1
    return ctr 

def findTail(head):
    curr=head
    if curr==None:
        return None
    while curr.nxt!=None:
        curr=curr.nxt 
    return curr

def partition2(obj,x):
    length=getLen(obj.head)
    tail=findTail(obj.head)
    mockNode=Node(-1,obj.head) # points to head
    curr=mockNode
    newHeadFound=False
    for i in range(length):
        if curr.nxt.val>=x:
            tail.nxt=curr.nxt
            tail=tail.nxt 
            curr.nxt=curr.nxt.nxt 
            tail.nxt=None
        else:
            if not newHeadFound:
                obj.head=curr.nxt
                newHeadFound=True
            curr=curr.nxt 

obj=MyLL()
obj.addAtTail(12)
obj.addAtTail(15)
obj.addAtTail(7)
obj.addAtTail(8)
obj.addAtTail(5)
obj.addAtTail(9)
obj.addAtTail(3)
obj.addAtTail(12)
obj.addAtTail(9)
obj.addAtTail(20)
print(obj)
partition2(obj,9)
print(obj)
obj2=MyLL()
print(obj2)
partition2(obj2,9)
print(obj2)
obj3=MyLL()
obj3.addAtTail(30)
obj3.addAtTail(40)
obj3.addAtTail(50)
obj3.addAtTail(60)
print(obj3)
partition2(obj3,9)
print(obj3)

def partition(ll, x):
    current = ll.tail = ll.head

    while current:
        next_node = current.next
        current.next = None
        if current.value < x:
            current.next = ll.head
            ll.head = current
        else:
            ll.tail.next = current
            ll.tail = current
        current = next_node

    # Error check in case all nodes are less than x
    if ll.tail.next is not None:
        ll.tail.next = None


def example():

    ll = LinkedList.generate(10, 0, 99)
    print(ll)
    partition(ll, ll.head.value)
    print(ll)
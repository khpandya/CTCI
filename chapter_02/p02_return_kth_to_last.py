from linked_list import LinkedList
from LL import MyLL

def getLen(ll):
    curr=ll.head
    if curr==None:
        return 0
    count=1
    while curr.nxt!=None:
        curr=curr.nxt
        count+=1
    return count

def getIndex(index,ll):
    curr=ll.head
    count=1
    while count!=index:
        curr=curr.nxt
        count+=1
    return curr.val

def k(ll,k):
    print('ran2')
    length=getLen(ll)
    if k<1 or k>length:
        return None
    index=length-(k-1)
    return getIndex(index,ll)

obj=MyLL()
obj.addAtTail(10)
obj.addAtTail(20)
obj.addAtTail(30)
obj.addAtTail(40)
obj.addAtTail(50)
print(obj)
print(k(obj,1))
print(k(obj,5))



def kth_to_last(ll, k):
    print('ran1')
    runner = current = ll.head
    for _ in range(k):
        if not runner:
            return None
        runner = runner.next

    while runner:
        current = current.next
        runner = runner.next

    return current


test_cases = (
    # list, k, expected
    ((10, 20, 30, 40, 50), 1, 50),
    ((10, 20, 30, 40, 50), 5, 10),
)


def test_kth_to_last():
    for linked_list_values, k, expected in test_cases:
        ll = LinkedList(linked_list_values)
        assert k(ll, k).value == expected



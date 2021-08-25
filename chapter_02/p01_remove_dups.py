import time
from LL import MyLL
from linked_list import LinkedList

def removeDupes(ll):
    vE={}
    curr=ll.head
    
    if curr!=None:
        vE[curr.val]=curr.val
    else:
        return None
    
    while curr.nxt!=None:
        if curr.nxt.val not in vE:
            vE[curr.nxt.val]=curr.nxt.val
            curr=curr.nxt
        else:
            deleteNextNode(curr)


def removeDupes2(ll):
    slow=ll.head
    if slow==None:
        return None
    while slow!=None and slow.nxt!=None:
        fast=slow
        while fast.nxt!=None:
            if fast.nxt.val==slow.val:
                deleteNextNode(fast)
            else:
                fast=fast.nxt
        slow=slow.nxt

def removeNegs(ll):
    curr=ll.head
    if curr==None:
        return None
    while(curr!=None):
        if curr.val<0:
            curr=curr.nxt
        else:
            break
    if curr==None:
        return
    ll.head=curr
    while curr.nxt!=None:
        if curr.nxt.val<0:
            curr.nxt=curr.nxt.nxt
        else:
            curr=curr.nxt 
    


def deleteNextNode(curr):
    curr.nxt=curr.nxt.nxt

# test 3->1->5->1->3->3->4->0->4 should be 3->1->5->4->0
obj=MyLL()
obj.addAtTail(-3)
obj.addAtTail(-11)
obj.addAtTail(5)
obj.addAtTail(1)
obj.addAtTail(3)
obj.addAtTail(3)
obj.addAtTail(-4)
obj.addAtTail(0)
obj.addAtTail(-4)
print(obj)
removeNegs(obj)
print(obj)

# test 1-1-1-1 becomes 1
obj2=MyLL()
obj2.addAtTail(1)
obj2.addAtTail(1)
obj2.addAtTail(1)
obj2.addAtTail(1)
print(obj2)
removeDupes2(obj2)
print(obj2)

# test empty is empty
obj3=MyLL()
removeDupes2(obj3)
print(obj3)

def remove_dups(ll):
    current = ll.head
    previous = None
    seen = set()

    while current:
        if current.value in seen:
            previous.next = current.next
        else:
            seen.add(current.value)
            previous = current
        current = current.next
    ll.tail = previous
    return ll


def remove_dups_followup(ll):
    runner = current = ll.head
    while current:
        runner = current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next
    ll.tail = runner
    return ll


testable_functions = (remove_dups, remove_dups_followup)
test_cases = (
    ([], []),
    ([1, 1, 1, 1, 1, 1], [1]),
    ([1, 2, 3, 2], [1, 2, 3]),
    ([1, 2, 2, 3], [1, 2, 3]),
    ([1, 1, 2, 3], [1, 2, 3]),
    ([1, 2, 3], [1, 2, 3]),
)


def test_remove_dupes():
    for f in testable_functions:
        start = time.perf_counter()
        for _ in range(100):
            for values, expected in test_cases:
                expected = expected.copy()
                deduped = f(LinkedList(values))
                assert deduped.values() == expected

                deduped.add(5)
                expected.append(5)
                assert deduped.values() == expected

        duration = time.perf_counter() - start
        print(f"{f.__name__} {duration * 1000:.1f}ms")


def example():
    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    remove_dups(ll)
    print(ll)

    ll = LinkedList.generate(100, 0, 9)
    print(ll)
    remove_dups_followup(ll)
    print(ll)

class MyLL:
    # singly linked list with the following things
    # head, val, nxt, print(), get(index), addAtHead(), addAtTail(), addAtIndex(index,value), deleteAtIndex(index)
    # try to use only head, val, nxt and print for testing
    
    def __init__(self):
        """
        Initialize your data structure here.
        """
        
        # why initialize head with None instead of a Node with a null value and next=None? Because when its just initialized
        # it'll have a Node object (!=None) with a None value at head so if you call addAtHead or addAtTail 
        # it'll do NodeWithNone->1 or 1->NodeWithNone instead of just setting head to 1 
        
        self.head=None
    
    def __str__(self):
        curr=self.head
        string=""
        if curr==None:
            return "empty"
        while curr.nxt!=None:
            string+=(str(curr.val)+"->")
            curr=curr.nxt
        string+=str(curr.val)
        return string

    def get(self, index: int):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        curr=self.head
        count=0
        while count<index and curr.nxt!=None:
            curr=curr.nxt
            count+=1
        if count==index:
            return curr.val
        else:
            return -1
        

    def addAtHead(self, val: int):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """
        curr=self.head
        if curr==None:
            self.head=Node(val,None)
            return None
        self.head=Node(val,self.head)

    def addAtTail(self, val: int):
        """
        Append a node of value val to the last element of the linked list.
        """
        curr=self.head
        if curr==None:
            self.head=Node(val,None)
            return None
        while curr.nxt!=None:
            curr=curr.nxt
        curr.nxt=Node(val,None)
        

    def addAtIndex(self, index: int, val: int):
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """
        if index==0:
            self.addAtHead(val)
            return None
        curr=self.head
        count=0
        while (count+1)!=index and curr.nxt!=None:
            curr=curr.nxt
            count+=1
        if count+1==index:
            if curr.nxt==None:
                self.addAtTail(val)
            else:
                add=Node(val,curr.nxt)
                curr.nxt=add
                    
    def deleteAtIndex(self, index: int):
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index==0:
            self.head=self.head.nxt
            return None
        curr=self.head
        count=0
        while count+1!=index and curr.nxt!=None:
            curr=curr.nxt
            count+=1
        if count+1==index and curr.nxt!=None:
            curr.nxt=curr.nxt.nxt
        
class Node:
    
    def __init__(self,val,nxt=None):
        self.val=val
        self.nxt=nxt

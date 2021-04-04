class Node:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.left = None
        self.right = None

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        #1 listen
        #2 Example. 1) given 2) null becomes 5
        #3 Brute Force - start at root, if key>r go right, else go left. stop when you want
        # to go left or right but its None, and put it there.
        curr=root
        if curr is None:
            root=TreeNode(val)
            return root
        while curr!=None:
            if val>curr.val:
                if curr.right!=None:
                    curr=curr.right
                else:
                    curr.right=TreeNode(val)
                    break
            else:
                if curr.left!=None:
                    curr=curr.left
                else:
                    curr.left=TreeNode(val)
                    break
        return root
        

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        new = Node(key)
        if self.root is None:
            self.root = new
            return

        current = self.root
        while current:
            if current.key > key:
                if current.left is None:
                    current.left = new
                    new.parent = current
                    return
                current = current.left
            else:
                if current.right is None:
                    current.right = new
                    new.parent = current
                    return
                current = current.right

    def get_node(self, key):
        current = self.root
        while current:
            if current.key == key:
                return current

            if current.key > key:
                current = current.left
            else:
                current = current.right
        raise Exception("No such value in the tree")


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(20)
    bst.insert(9)
    bst.insert(25)
    bst.insert(5)
    bst.insert(12)
    bst.insert(11)
    bst.insert(14)

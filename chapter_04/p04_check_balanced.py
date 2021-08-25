class BinaryNode:
    def __init__(self, name):
        self.name = name
        self.left = None
        self.right = None


# easy to understand brute-force solution O(n^2) using definition of balanced tree
# this is equivalent to starting from the top, checking height of root left subtree, checking height of root right ST
# calculating the difference, then doing that again for left child and right child till we check each node has balanced condition
# especially note the way to calculate depth of subtree, useful common construct
# get depth of left and right subtree and check if difference<=1, then check the same for both child nodes
# note that we are recalculating depth everytime by traversing both subtrees at each node
class Solution:
    def depth(self,root):
        if root==None:
            return 0
        return max(self.depth(root.left),self.depth(root.right))+1
        
    
    def isBalanced(self, root):
        if root==None: # base case - null node is balanced
            return True
        
        if abs(self.depth(root.left)-self.depth(root.right))<2 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True

# better O(n) solution
# this is equivalent to starting at the bottom (leaf), checking if its balanced and storing height of subtree with root=this node
# then we go up one level, height of left and right subtree are already available from previous check so its just a matter of taking
# the difference and checking if its <2, and again we store height=max(left ST, right ST)+1 as the height of the current ST
# a single element list is passed to depth to act as a shared boolean flag across calls - if one of the nodes is found to be imbalanced
# this flag is turned to false, once the main call has ended we can check if the flag is still true (implies all nodes were balanced)
# otherwise the tree is imbalanced
# note that in a way we are just modifying the depth function from previous solution to check balanced as we go
class Solution:
    # read this function bottom to top
    def depth(self,root,lst):
        if root==None: # base case for calculating height
            return 0

        if not lst[0]: # once the boolean flag is false, none of the other checks/calls actually matter - we have already discovered
            return -1 # that the tree is imbalanced. This if condition isn't necessary but helps to terminate all calls faster and stops
        # all the balance-checking we would do on other calls if we didn't return immediately. So it helps to exit the main call so we can
        # just return false quickly. The -1 has no special significance, we can return anything - its only for the sake of exiting faster
        # returning a number is necessary however since abs(left-right) will fail if one of the calls returned a non-number

        leftHeight=self.depth(root.left,lst)  # as we move up the call stack, we will quickly get the depth as +1 from lower level
        rightHeight=self.depth(root.right,lst)
        if abs(leftHeight-rightHeight)>=2: # if imbalanced, turn flag false
            lst[0]=False

        return max(leftHeight,rightHeight)+1 # so leaf returns 1 and so on (first line base case gives 0 for null nodes)

    def isBalanced(self, root: TreeNode):
        lst=[True]
        self.depth(root,lst) # process root through depth function and check if the boolean flag is still true
        return lst[0]


def is_balanced(node):

    if node.left and node.right:
        return is_balanced(node.left) and is_balanced(node.right)

    if node.left:  # but not node.right
        if node.left.left or node.left.right:
            return False  # two layers, unbalanced

    if node.right:
        if node.right.left or node.right.right:
            return False

    return True


def test_is_balanced():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    assert is_balanced(root)
    root.left.left = BinaryNode(4)
    assert not is_balanced(root)


def example():
    root = BinaryNode(1)
    root.left = BinaryNode(2)
    print(is_balanced(root))
    root.left.left = BinaryNode(4)
    root.left.right = BinaryNode(5)
    root.left.right.right = BinaryNode(6)
    root.left.right.right.right = BinaryNode(7)
    root.right = BinaryNode(3)
    root.right.left = BinaryNode(8)
    root.right.right = BinaryNode(9)
    root.right.right.right = BinaryNode(10)
    root.right.right.right.right = BinaryNode(11)
    print(is_balanced(root))


if __name__ == "__main__":
    example()

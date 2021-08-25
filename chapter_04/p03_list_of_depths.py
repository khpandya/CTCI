from collections import deque

# from linked_list import LinkedList

#LC
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

root=TreeNode(7)
lvl10=TreeNode(-7)
root.left=lvl10
lvl11=TreeNode(8)
root.right=lvl11
lvl20=TreeNode(-3)
lvl11.left=lvl20
lvl21=TreeNode(6)
lvl11.right=lvl21
lvl3=TreeNode(9)
lvl20.right=lvl3
lvl4=TreeNode(-5)
lvl3.right=lvl4
def levelOrder(self, root):
    if root==None:
        return []
    levels={0:[root]}
    lastLevel=False
    level=0
    while(not lastLevel):
        for node in levels[level]:
            if node.left:
                if level+1 in levels:
                    levels[level+1].append(node.left)
                else:
                    levels[level+1]=[node.left]
            if node.right:
                if level+1 in levels:
                    levels[level+1].append(node.right)
                else:
                    levels[level+1]=[node.right]
        if level+1 not in levels:
            lastLevel=True
        level+=1
    
    result=[[] for level in levels]
    for level in levels:
        for node in levels[level]:
            result[level].append(node.val)
    
    return result

levelOrder(root)
# { [TreeNode{val: 7, 
#           left: TreeNode{val: -7}
#           right: TreeNode{val: 8, 
#               left: TreeNode{val: -3, 
#                   left: None, 
#                   right: TreeNode{val: 9, 
#                       left: None, 
#                       right: TreeNode{val: -5, 
#                           left: None, 
#                           right: None}}}, 
#               right: TreeNode{val: 6, left: None, right: None}}}], 
# 1: #-7,8 [TreeNode{val: -7, left: None, right: None}, TreeNode{val: 8, left: TreeNode{val: -3, left: None, right: TreeNode{val: 9, left: None, right: TreeNode{val: -5, left: None, right: None}}}, right: TreeNode{val: 6, left: None, right: None}}], 
# 2:#N,N,-3,6 [None, None, TreeNode{val: -3, left: None, right: TreeNode{val: 9, left: None, right: TreeNode{val: -5, left: None, right: None}}}, TreeNode{val: 6, left: None, right: None}], 
# 3:#N,9,N,N [None, TreeNode{val: 9, left: None, right: TreeNode{val: -5, left: None, right: None}}, None, None], 
# 4: []#should be -5
# #should be level 5 with N,N}
class BinaryNode:
    def __init__(self, name, left=None, right=None):
        self.name = name
        self.left = left
        self.right = right


def create_node_list_by_depth(tree_root):
    # BFS.
    levels = {}
    q = deque()
    q.append((tree_root, 0))

    while len(q) > 0:
        node, level = q.popleft()
        if level not in levels:
            # First node in the level
            levels[level] = LinkedList()
        # Nodes already exist
        levels[level].add(node)

        # Push onto queue
        if node.left:
            q.append((node.left, level + 1))
        if node.right:
            q.append((node.right, level + 1))
    return levels


def create_node_list_by_depth_b(tree):
    if not tree:
        return []

    curr = tree
    result = [LinkedList([curr])]
    level = 0

    while result[level]:
        result.append(LinkedList())
        for linked_list_node in result[level]:
            n = linked_list_node.value
            if n.left:
                result[level + 1].add(n.left)
            if n.right:
                result[level + 1].add(n.right)
        level += 1
    return result


testable_functions = [create_node_list_by_depth, create_node_list_by_depth_b]


def test_create_node_list_by_depth():
    for f in testable_functions:
        node_h = BinaryNode("H")
        node_g = BinaryNode("G")
        node_f = BinaryNode("F")
        node_e = BinaryNode("E", node_g)
        node_d = BinaryNode("D", node_h)
        node_c = BinaryNode("C", None, node_f)
        node_b = BinaryNode("B", node_d, node_e)
        node_a = BinaryNode("A", node_b, node_c)
        lists = f(node_a)

        assert lists[0].values() == LinkedList([node_a]).values()
        assert lists[1].values() == LinkedList([node_b, node_c]).values()
        assert lists[2].values() == LinkedList([node_d, node_e, node_f]).values()
        assert lists[3].values() == LinkedList([node_h, node_g]).values()


def example():
    root = BinaryNode(0)
    root.left = BinaryNode(1)
    root.right = BinaryNode(2)
    root.left.left = BinaryNode(3)
    root.left.right = BinaryNode(4)
    root.right.left = BinaryNode(5)
    root.right.right = BinaryNode(6)

    levels = create_node_list_by_depth(root)
    print(levels)


if __name__ == "__main__":
    # example()
    pass
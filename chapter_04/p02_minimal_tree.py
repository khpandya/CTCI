class Node:
    def __init__(self, item):
        self.right = None
        self.left = None
        self.val = item

    def disp(self, nesting=0):
        indent = " " * nesting * 2
        output = f"{self.val}\n"
        if self.left is not None:
            output += f"{indent}L:"
            output += self.left.disp(nesting + 1)
        if self.right is not None:
            output += f"{indent}R:"
            output += self.right.disp(nesting + 1)
        return output

    def __str__(self):
        return self.disp()

# best LC solution, without python slices
class solution:
    def sortedArrayToBST(self, nums):
            return self.helper(nums, 0, len(nums))

    def helper(self, nums, lower, upper):
        if lower == upper: # only tricky part is to catch that lower==upper is the case to terminate
            return None

        mid = (lower + upper) // 2
        node = TreeNode(nums[mid])
        node.left = self.helper(nums, lower, mid)
        node.right = self.helper(nums, mid+1, upper)

        return node

# easier but slower using slices
def sortedArrayToBST(self, num):
        if not num:
            return None

        mid = len(num) // 2

        root = TreeNode(num[mid])
        root.left = self.sortedArrayToBST(num[:mid])
        root.right = self.sortedArrayToBST(num[mid+1:])

        return root

def array_to_binary_tree(array, start, end):
    if start > end:
        return None
    mid = (
        start + end
    ) // 2  # This must be floor division, otherwise you get a slice error
    # TypeError: list indices must be integers or slices, not float
    root = Node(array[mid])
    root.left = array_to_binary_tree(array, start, mid - 1)
    root.right = array_to_binary_tree(array, mid + 1, end)
    return root


if __name__ == "__main__":
    test_array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 15, 18, 22, 43, 144, 515, 4123]
    print(minimalTree(test_array))

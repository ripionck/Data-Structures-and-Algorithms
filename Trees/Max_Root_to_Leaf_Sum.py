class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def max_root_to_leaf_sum(root):
    if root is None:
        return 0
    left_sum = max_root_to_leaf_sum(root.left)
    right_sum = max_root_to_leaf_sum(root.right)
    return root.val + max(left_sum, right_sum)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

max_sum = max_root_to_leaf_sum(root)
print("Maximum root-to-leaf path sum:", max_sum)


# time complexity --- O(n)

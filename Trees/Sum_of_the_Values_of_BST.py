class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def sum_of_values(root):
    if root is None:
        return 0
    return root.val + sum_of_values(root.left) + sum_of_values(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


total_sum = sum_of_values(root)
print("Sum of all values in the binary tree:", total_sum)

# O(n)

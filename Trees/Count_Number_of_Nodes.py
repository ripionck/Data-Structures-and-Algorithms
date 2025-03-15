class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def count_nodes(root):
    if root is None:
        return 0
    return 1 + count_nodes(root.left) + count_nodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

total_nodes = count_nodes(root)
print("Total number of nodes in the binary tree:", total_nodes)


# time complexity -- O(n)

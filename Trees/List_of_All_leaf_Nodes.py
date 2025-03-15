class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_leaves(root):
    def dfs(node, leaves):
        if node is None:
            return
        if node.left is None and node.right is None:
            leaves.append(node.val)
        dfs(node.left, leaves)
        dfs(node.right, leaves)

    leaves = []
    dfs(root, leaves)
    return leaves


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

leaves = find_leaves(root)
print("List of leaf nodes in the binary tree:", leaves)

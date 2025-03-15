class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def in_order_traversal(root):
    if root:
        in_order_traversal(root.left)
        print(root.val, end=' ')
        in_order_traversal(root.right)


def pre_order_traversal(root):
    if root:
        print(root.val, end=' ')
        pre_order_traversal(root.left)
        pre_order_traversal(root.right)


def post_order_traversal(root):
    if root:
        post_order_traversal(root.left)
        post_order_traversal(root.right)
        print(root.val, end=' ')


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("In-order traversal:")
in_order_traversal(root)

print("Pre-order traversal:")
pre_order_traversal(root)

print("Post-order traversal:")
post_order_traversal(root)

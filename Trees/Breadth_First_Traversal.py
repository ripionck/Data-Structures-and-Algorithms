class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def breadth_first_traversal(root):
    if root is None:
        return

    queue = []
    queue.append(root)

    while queue:
        node = queue.pop(0)
        print(node.val, end=' ')

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Breadth first traversal:")
breadth_first_traversal(root)

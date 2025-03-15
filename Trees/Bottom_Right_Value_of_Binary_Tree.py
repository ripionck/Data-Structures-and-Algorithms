from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_bottom_right_value(root):
    if root is None:
        return None

    queue = deque([root])
    bottom_right_value = None

    while queue:
        node = queue.popleft()
        bottom_right_value = node.val
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return bottom_right_value


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

bottom_right = find_bottom_right_value(root)
print("Bottom-right value in the binary tree:", bottom_right)

from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Iterative approach
"""def tree_includes(root, target):
    if root is None:
        return False

    queue = deque([root])

    while queue:
        current = queue.popleft()
        if current.val == target:
            return True
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return False"""


def tree_includes(root, target):
    if root is None:
        return False
    if root.val == target:
        return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

target = 5
print("Tree includes", target, ":", tree_includes(root, target))


#  O(n)

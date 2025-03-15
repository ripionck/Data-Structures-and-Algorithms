from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def tree_levels(root):
    if root is None:
        return []

    levels = []
    queue = deque([(root, 0)])

    while queue:
        node, level = queue.popleft()
        if len(levels) == level:
            levels.append([])
        levels[level].append(node.val)

        if node.left:
            queue.append((node.left, level+1))

        if node.right:
            queue.append((node.right, level+1))

    return levels


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

levels = tree_levels(root)
print("Levels of the binary tree:")
for i, level in enumerate(levels):
    print(f"Level {i}: {level}")

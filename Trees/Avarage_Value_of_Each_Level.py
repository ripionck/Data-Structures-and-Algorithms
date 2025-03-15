from collections import deque


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def level_averages(root):
    if root is None:
        return []

    averages = []
    queue = deque([root])

    while queue:
        level_length = len(queue)
        level_sum = 0

        for _ in range(level_length):
            node = queue.popleft()
            level_sum += node.val
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        averages.append(level_sum / level_length)

    return averages


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)

averages = level_averages(root)
print("Average values at each level of the binary tree:", averages)

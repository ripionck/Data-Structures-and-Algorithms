from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def left_view_recursive(root):
    result = []

    def dfs(node, level):
        if not node:
            return

        if len(result) == level:
            result.append(node.val)

        dfs(node.left, level + 1)
        dfs(node.right, level + 1)

    dfs(root, 0)
    return result


def left_view_iterative(root):
    if not root:
        return []

    result = []
    queue = deque([(root, 0)])

    while queue:
        level_size = len(queue)
        for i in range(level_size):
            node, level = queue.popleft()

            if len(result) == level:
                result.append(node.val)

            if node.left:
                queue.append((node.left, level + 1))
            if node.right:
                queue.append((node.right, level + 1))

    return result


# Create a sample binary tree
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(5)
root.right.right = TreeNode(6)
root.right.left.left = TreeNode(7)

# Use the recursive method
print(left_view_recursive(root))  # Output: [1, 2, 4, 7]

# Use the iterative method
print(left_view_iterative(root))  # Output: [1, 2, 4, 7]

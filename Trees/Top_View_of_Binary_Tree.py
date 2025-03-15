from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def top_view(root):
    if not root:
        return []

    # Dictionary to store the topmost node for each horizontal distance
    top_nodes = {}

    # Queue for level order traversal
    # Each element is (node, horizontal_distance)
    queue = deque([(root, 0)])

    # To keep track of the range of horizontal distances
    min_hd = max_hd = 0

    while queue:
        node, hd = queue.popleft()

        # Only add to top_nodes if this horizontal distance hasn't been seen before
        if hd not in top_nodes:
            top_nodes[hd] = node.val

        # Update the range of horizontal distances
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        # Add left child to queue with hd - 1
        if node.left:
            queue.append((node.left, hd - 1))

        # Add right child to queue with hd + 1
        if node.right:
            queue.append((node.right, hd + 1))

    # Construct the top view from left to right
    return [top_nodes[i] for i in range(min_hd, max_hd + 1)]


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.right = TreeNode(4)
root.left.right.right = TreeNode(5)
root.left.right.right.right = TreeNode(6)

print(top_view(root))

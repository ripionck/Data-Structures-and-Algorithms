from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def bottom_view(root):
    if not root:
        return []

    # Dictionary to store the bottommost node for each horizontal distance
    bottom_nodes = {}

    # Queue for level order traversal
    # Each element is (node, horizontal_distance)
    queue = deque([(root, 0)])

    # To keep track of the range of horizontal distances
    min_hd = max_hd = 0

    while queue:
        node, hd = queue.popleft()

        # Update the bottommost node for this horizontal distance
        bottom_nodes[hd] = node.val

        # Update the range of horizontal distances
        min_hd = min(min_hd, hd)
        max_hd = max(max_hd, hd)

        # Add left child to queue with hd - 1
        if node.left:
            queue.append((node.left, hd - 1))

        # Add right child to queue with hd + 1
        if node.right:
            queue.append((node.right, hd + 1))

    # Construct the bottom view from left to right
    return [bottom_nodes[i] for i in range(min_hd, max_hd + 1)]


# Create a sample binary tree
root = TreeNode(20)
root.left = TreeNode(8)
root.right = TreeNode(22)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.right = TreeNode(25)
root.left.right.left = TreeNode(10)
root.left.right.right = TreeNode(14)

# Get the bottom view
print(bottom_view(root))  # Output: [5, 10, 3, 14, 25]

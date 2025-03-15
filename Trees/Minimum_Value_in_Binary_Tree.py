from collections import deque


class TreeNode:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None


def find_min_value(root):
    if root is None:
        return float('inf')  # Return a very large value for comparison
    left_min = find_min_value(root.left)
    right_min = find_min_value(root.right)
    return min(root.val, left_min, right_min)


# Iterative approach
def find_min_value(root):
    if root is None:
        return float('inf')

    min_value = float('inf')
    queue = deque([root])

    while queue:
        current = queue.popleft()
        if current.val < min_value:
            min_value = current.val
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)

    return min_value


root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)

min_value = find_min_value(root)
print(f"The minimum value in the BST is: {min_value}")


"""
The time complexity of this operation is O(h), where h is the height of the tree. In a balanced BST, this would be O(log n), where n is the number of nodes. In the worst case (a left-skewed tree), it could be O(n).
"""

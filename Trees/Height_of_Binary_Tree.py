class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def tree_height(root):
    if root is None:
        return -1  # Empty tree

    left_height = tree_height(root.left)
    right_height = tree_height(root.right)

    return max(left_height, right_height) + 1


root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)


tree_height = tree_height(root)
print(f"Height of the Binary Tree is: {tree_height}")


"""
The time complexity  is O(n) where n is the number of nodes in the tree, as we need to visit each node once.
The space complexity  is O(h) where h is the height of the tree, due to the recursion stack.

"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_path(root, target):
    def dfs(node, current_path):
        if node is None:
            return False
        current_path.append(node.val)
        if node.val == target:
            return True
        if dfs(node.left, current_path) or dfs(node.right, current_path):
            return True
        current_path.pop()
        return False

    path = []
    if dfs(root, path):
        return path
    else:
        return None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

target = 5
path = find_path(root, target)
if path:
    print(f"Path to node {target}:", path)
else:
    print(f"Node {target} not found in the tree.")

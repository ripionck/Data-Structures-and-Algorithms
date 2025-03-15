class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_paths(root):
    def dfs(node, current_path, all_paths):
        if node is None:
            return
        current_path.append(node.val)
        if node.left is None and node.right is None:
            all_paths.append(list(current_path))
        else:
            dfs(node.left, current_path, all_paths)
            dfs(node.right, current_path, all_paths)
        current_path.pop()

    all_paths = []
    dfs(root, [], all_paths)
    return all_paths


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


paths = find_paths(root)
print("All root to leaf paths:")
for path in paths:
    print(path)

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


def find_path_with_sum(root, target_sum):
    def dfs(node, current_path, current_sum):
        if node is None:
            return False
        current_path.append(node.val)
        current_sum += node.val
        if node.left is None and node.right is None and current_sum == target_sum:
            return True
        if dfs(node.left, current_path, current_sum) or dfs(node.right, current_path, current_sum):
            return True
        current_path.pop()
        return False

    path = []
    if dfs(root, path, 0):
        return path
    else:
        return None


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

target_sum = 7
path = find_path_with_sum(root, target_sum)
if path:
    print(f"Path with sum {target_sum}:", path)
else:
    print(f"No path with sum {target_sum} found in the tree.")

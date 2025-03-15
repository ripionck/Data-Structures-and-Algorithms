class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def insert(node, value):
    """
    Insert a new value into the BST
    Time Complexity: O(h) where h is the height of the tree
    """
    if node is None:
        return Node(value)
    if value == node.data:
        print("Value already exists")
        return node
    elif value < node.data:
        node.left = insert(node.left, value)
    else:
        node.right = insert(node.right, value)
    return node


def find_min(node):
    """
    Find the minimum value in the BST
    Used as a helper function for deletion
    """
    current = node
    while current.left is not None:
        current = current.left
    return current


def delete(node, value):
    """
    Delete a value from the BST
    Time Complexity: O(h) where h is the height of the tree
    """
    if node is None:
        return node

    # Search for the node to be deleted
    if value < node.data:
        node.left = delete(node.left, value)
    elif value > node.data:
        node.right = delete(node.right, value)
    else:
        # Case 1: Leaf node
        if node.left is None and node.right is None:
            return None

        # Case 2: Node with one child
        elif node.left is None:
            return node.right
        elif node.right is None:
            return node.left

        # Case 3: Node with two children
        # Get the inorder successor (smallest in the right subtree)
        successor = find_min(node.right)
        # Copy the successor's data to this node
        node.data = successor.data
        # Delete the successor
        node.right = delete(node.right, successor.data)

    return node


def search(node, value):
    """
    Search for a value in the BST
    Time Complexity: O(h) where h is the height of the tree
    """
    if node is None or node.data == value:
        return node

    if value < node.data:
        return search(node.left, value)
    return search(node.right, value)


def in_order_traversal(node):
    """
    Perform inorder traversal of the BST
    Time Complexity: O(n) where n is the number of nodes
    """
    if node is not None:
        in_order_traversal(node.left)
        print(node.data, end=' ')
        in_order_traversal(node.right)


if __name__ == "__main__":
    root = Node(5)

    # Insert nodes
    values_to_insert = [3, 7, 2, 4, 6, 8]
    for value in values_to_insert:
        root = insert(root, value)

    print("Inorder traversal of the BST:")
    in_order_traversal(root)  # Should print: 2 3 4 5 6 7 8
    print("\n")

    # Delete a node
    print("Deleting node with value 3")
    root = delete(root, 3)

    print("Inorder traversal after deletion:")
    in_order_traversal(root)  # Should print: 2 4 5 6 7 8
    print("\n")

    # Search for a value
    search_value = 6
    result = search(root, search_value)
    if result:
        print(f"Value {search_value} found in the BST")
    else:
        print(f"Value {search_value} not found in the BST")

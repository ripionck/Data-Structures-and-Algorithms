class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_node(self, node):
        # Note: This function assumes that the node to be deleted is not the last node in the list
        if not node or not node.next:
            return  # Cannot delete last node with this method

        # Copy data from the next node to the current node
        node.data = node.next.data

        # Delete the next node
        node.next = node.next.next

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)


# Example usage:
if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(1)
    ll.insert_at_end(2)
    ll.insert_at_end(3)
    ll.insert_at_end(4)
    ll.insert_at_end(5)

    print("Original list:", ll.display())

    # Delete the node with value 3 (assuming we have a reference to this node)
    node_to_delete = ll.head.next.next  # This is the node with value 3
    ll.delete_node(node_to_delete)

    print("After deleting node with value 3:", ll.display())

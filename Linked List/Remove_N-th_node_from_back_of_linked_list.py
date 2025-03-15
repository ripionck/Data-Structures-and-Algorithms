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

    def remove_nth_from_end(self, n):
        # Edge case: if the list is empty
        if not self.head:
            return

        # Use two pointers: fast and slow
        fast = slow = self.head

        # Move fast pointer n nodes ahead
        for _ in range(n):
            if not fast:
                return  # n is greater than the length of the list
            fast = fast.next

        # If fast is None, we need to remove the head
        if not fast:
            self.head = self.head.next
            return

        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next

        # Remove the nth node from the end
        slow.next = slow.next.next

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

    ll.remove_nth_from_end(2)  # Remove 2nd node from the end
    print("After removing 2nd node from the end:", ll.display())

    ll.remove_nth_from_end(1)  # Remove last node
    print("After removing last node:", ll.display())

    ll.remove_nth_from_end(3)  # Remove first node
    print("After removing first node:", ll.display())

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def insert_at_position(self, data, position):
        if position <= 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current is None:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_first(self):
        if not self.head:
            return None
        deleted_data = self.head.data
        self.head = self.head.next
        return deleted_data

    def delete_last(self):
        if not self.head:
            return None
        if not self.head.next:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_data = current.next.data
        current.next = None
        return deleted_data

    def delete_at_position(self, position):
        if not self.head:
            return None
        if position <= 0:
            return self.delete_first()
        current = self.head
        for _ in range(position - 1):
            if current.next is None:
                raise IndexError("Position out of range")
            current = current.next
        if current.next is None:
            raise IndexError("Position out of range")
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def search(self, data):
        current = self.head
        position = 0
        while current:
            if current.data == data:
                return position
            current = current.next
            position += 1

        return -1

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)


# Example usage:
if __name__ == "__main__":
    sll = SinglyLinkedList()
    sll.insert_at_end(1)
    sll.insert_at_end(2)
    sll.insert_at_end(3)
    sll.insert_at_beginning(0)
    sll.insert_at_position(1.5, 2)
    print("List:", sll.display())
    print("Search 2:", sll.search(2))
    print("Delete first:", sll.delete_first())
    print("Delete last:", sll.delete_last())
    print("Delete at position 1:", sll.delete_at_position(1))
    print("Final list:", sll.display())

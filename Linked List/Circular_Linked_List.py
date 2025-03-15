class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            new_node.next = self.head
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            new_node.next = new_node
            self.head = new_node
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = new_node
            new_node.next = self.head

    def insert_at_position(self, data, position):
        if position <= 0:
            self.insert_at_beginning(data)
            return
        new_node = Node(data)
        current = self.head
        for _ in range(position - 1):
            if current.next == self.head:
                raise IndexError("Position out of range")
            current = current.next
        new_node.next = current.next
        current.next = new_node

    def delete_first(self):
        if not self.head:
            return None
        deleted_data = self.head.data
        if self.head.next == self.head:
            self.head = None
        else:
            current = self.head
            while current.next != self.head:
                current = current.next
            current.next = self.head.next
            self.head = self.head.next
        return deleted_data

    def delete_last(self):
        if not self.head:
            return None
        if self.head.next == self.head:
            deleted_data = self.head.data
            self.head = None
            return deleted_data
        current = self.head
        while current.next.next != self.head:
            current = current.next
        deleted_data = current.next.data
        current.next = self.head
        return deleted_data

    def delete_at_position(self, position):
        if not self.head:
            return None
        if position <= 0:
            return self.delete_first()
        current = self.head
        for _ in range(position - 1):
            if current.next == self.head:
                raise IndexError("Position out of range")
            current = current.next
        if current.next == self.head:
            raise IndexError("Position out of range")
        deleted_data = current.next.data
        current.next = current.next.next
        return deleted_data

    def search(self, data):
        if not self.head:
            return -1
        current = self.head
        position = 0
        while True:
            if current.data == data:
                return position
            current = current.next
            position += 1
            if current == self.head:
                break
        return -1

    def display(self):
        if not self.head:
            return "Empty list"
        elements = []
        current = self.head
        while True:
            elements.append(str(current.data))
            current = current.next
            if current == self.head:
                break
        return " -> ".join(elements) + " -> (head)"


# Example usage:
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_end(1)
    cll.insert_at_end(2)
    cll.insert_at_end(3)
    cll.insert_at_beginning(0)
    cll.insert_at_position(1.5, 2)
    print("List:", cll.display())
    print("Search 2:", cll.search(2))
    print("Delete first:", cll.delete_first())
    print("Delete last:", cll.delete_last())
    print("Delete at position 1:", cll.delete_at_position(1))
    print("Final list:", cll.display())

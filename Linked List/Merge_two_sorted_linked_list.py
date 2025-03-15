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

    def display(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return " -> ".join(elements)


def merge_sorted_lists(list1, list2):
    dummy = Node(0)
    current = dummy

    while list1 and list2:
        if list1.data <= list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next
        current = current.next

    if list1:
        current.next = list1
    if list2:
        current.next = list2

    merged_list = LinkedList()
    merged_list.head = dummy.next
    return merged_list


# Example usage:
if __name__ == "__main__":
    # Create first sorted linked list
    list1 = LinkedList()
    list1.insert_at_end(1)
    list1.insert_at_end(3)
    list1.insert_at_end(5)

    # Create second sorted linked list
    list2 = LinkedList()
    list2.insert_at_end(2)
    list2.insert_at_end(4)
    list2.insert_at_end(6)

    print("List 1:", list1.display())
    print("List 2:", list2.display())

    # Merge the sorted lists
    merged_list = merge_sorted_lists(list1.head, list2.head)
    print("Merged List:", merged_list.display())

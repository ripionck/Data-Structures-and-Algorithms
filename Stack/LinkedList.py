class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class StackUsingLinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def pop(self):
        if self.head is None:
            return None
        popped_value = self.head.value
        self.head = self.head.next
        return popped_value

    def top(self):
        if self.head is None:
            return None
        return self.head.value

    def empty(self):
        return self.head is None


stack = StackUsingLinkedList()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False

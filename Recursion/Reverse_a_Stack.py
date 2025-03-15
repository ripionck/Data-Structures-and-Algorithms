class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None

    # def insert_at_bottom(self, item):
    #     if self.is_empty():
    #         self.push(item)

    #     else:
    #         temp = self.pop()
    #         self.insert_at_bottom(item)
    #         self.push(temp)

    # def reverse(self):
    #     if not self.is_empty():
    #         temp = self.pop()
    #         self.reverse()
    #         self.insert_at_bottom(temp)

    # Using an auxiliary stack

    def reverse(self):
        auxiliary_stack = Stack()
        while not self.is_empty():
            auxiliary_stack.push(self.pop())
        self.items = auxiliary_stack.items

    def __str__(self):
        return str(self.items)


stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)
print("Original stack:", stack)
stack.reverse()
print("Reversed stack:", stack)

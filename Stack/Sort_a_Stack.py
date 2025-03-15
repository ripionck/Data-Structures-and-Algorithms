class Stack:
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.empty():
            return None
        return self.stack.pop()

    def top(self):
        if self.empty():
            return None
        return self.stack[-1]

    def empty(self):
        return len(self.stack) == 0


"""
Use an auxiliary stack to hold elements in sorted order.
Transfer elements from the original stack to the auxiliary stack, ensuring the auxiliary stack remains sorted.
Finally, transfer the sorted elements back to the original stack.
"""


def sort_stack(original_stack):
    auxiliary_stack = Stack()

    while not original_stack.empty():
        temp = original_stack.pop()

        while not auxiliary_stack.empty() and auxiliary_stack.top() > temp:
            original_stack.push(auxiliary_stack.pop())

        auxiliary_stack.push(temp)

    while not auxiliary_stack.empty():
        original_stack.push(auxiliary_stack.pop())


stack = Stack()
stack.push(34)
stack.push(3)
stack.push(31)
stack.push(98)
stack.push(92)
stack.push(23)

print("Original Stack:")
print(stack.stack)

sort_stack(stack)

print("Sorted Stack:")
print(stack.stack)

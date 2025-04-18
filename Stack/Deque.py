from collections import deque

class Stack:
    def __init__(self):
        self.container = deque()

    def is_empty(self):
        return len(self.container) == 0

    def push(self, item):
        self.container.append(item)

    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return str(self.container)
    
if __name__ == "__main__":
    stack = Stack()

    print("Is stack empty?", stack.is_empty())

    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Stack:", stack)
    print("Top item:", stack.peek())
    print("Stack size:", stack.size())

    print("Popped:", stack.pop())
    print("Stack:", stack)
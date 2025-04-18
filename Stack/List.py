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
        raise IndexError("Pop from empty stack")
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Peek from empty stack")
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        return str(self.items)
    

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
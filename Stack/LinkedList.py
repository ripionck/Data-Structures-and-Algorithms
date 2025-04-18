class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        popped_item = self.top.data
        self.top = self.top.next
        self._size -= 1
        return popped_item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self.top.data
    
    def is_empty(self):
        return self.top is None
    
    def size(self):
        return self._size
    
    def __str__(self):
        items = []
        current = self.top
        while current:
            items.append(str(current.data))
            current = current.next
        return "->".join(reversed(items)) if items else "Empty stack"
    

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
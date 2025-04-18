class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self, item):
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Dequeue from empty queue")
        removed_item = self.front.data
        self.front = self.front.next
        self._size -= 1
        if self.is_empty():
            self.rear = None
        return removed_item
    
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty queue")
        return self.front.data
    
    def is_empty(self):
        return self.front is None
    
    def size(self):
        return self._size
    
    def __str__(self):
        items = []
        current = self.front
        while current:
            items.append(str(current.data))
            current = current.next
        return "->".join(items) if items else "Empty queue"
    

if __name__ == "__main__":
    q = Queue()

    print("Is queue empty?", q.is_empty())

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue:", q)
    print("Front item:", q.peek())
    print("Queue size:", q.size())

    print("Dequeued:", q.dequeue())
    print("Queue:", q)
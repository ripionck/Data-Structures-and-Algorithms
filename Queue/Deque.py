from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()

    def enqueue(self, item):
        self.container.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.container.popleft()
        raise IndexError("Dequeue from empty queue")
    
    def front(self):
        if not self.is_empty():
            return self.container[0]
        raise IndexError("Front from empty queue")
    
    def is_empty(self):
        return len(self.container) == 0
    
    def size(self):
        return len(self.container)
    
    def __str__(self):
        return f"Queue({list(self.container)})"
    


if __name__ == "__main__":
    q = Queue()

    print("Is queue empty?", q.is_empty())

    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)

    print("Queue:", q)
    print("Front item:", q.front())
    print("Queue size:", q.size())

    print("Dequeued:", q.dequeue())
    print("Queue:", q)
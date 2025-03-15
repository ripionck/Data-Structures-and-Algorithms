class QueueUsingStacks:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def enqueue(self, item):
        self.stack1.append(item)
        print(f"Enqueued: {item}")

    def dequeue(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        if not self.stack2:
            print("Queue is empty")
            return None
        item = self.stack2.pop()
        print(f"Dequeued: {item}")
        return item

    def is_empty(self):
        return not self.stack1 and not self.stack2

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print("Queue:", end=" ")
            for item in self.stack2[::-1]:
                print(item, end=" ")
            for item in self.stack1:
                print(item, end=" ")
            print()


q = QueueUsingStacks()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()

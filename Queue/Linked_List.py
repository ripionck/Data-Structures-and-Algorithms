class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
            print(f"Enqueued: {item}")
            return
        self.rear.next = new_node
        self.rear = new_node
        print(f"Enqueued: {item}")

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        print(f"Dequeued: {temp.data}")
        return temp.data

    def display(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            current = self.front
            print("Queue:", end=" ")
            while current:
                print(current.data, end=" ")
                current = current.next
            print()


q = Queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.display()
q.dequeue()
q.display()

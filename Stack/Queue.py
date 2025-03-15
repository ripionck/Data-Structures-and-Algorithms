from queue import Queue


class StackUsingQueues:
    def __init__(self):
        self.queue1 = Queue()
        self.queue2 = Queue()

    def push(self, x):
        self.queue2.put(x)
        while not self.queue1.empty():
            self.queue2.put(self.queue1.get())
        self.queue1, self.queue2 = self.queue2, self.queue1

    def pop(self):
        if self.queue1.empty():
            return None
        return self.queue1.get()

    def top(self):
        if self.queue1.empty():
            return None
        return self.queue1.queue[0]

    def empty(self):
        return self.queue1.empty()


stack = StackUsingQueues()
stack.push(1)
stack.push(2)
print(stack.top())  # Output: 2
print(stack.pop())  # Output: 2
print(stack.empty())  # Output: False

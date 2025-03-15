class Deque:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def add_front(self, item):
        self.items.append(item)

    def add_rear(self, item):
        self.items.insert(0, item)

    def remove_front(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def remove_rear(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            return None

    def size(self):
        return len(self.items)


deque = Deque()
deque.add_front(1)
deque.add_rear(2)
print(deque.remove_front())  # Output: 1
print(deque.remove_rear())   # Output: 2

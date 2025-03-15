class Heap:
    def __init__(self):
        self.heap = []

    def push(self, value):
        self.heap.append(value)
        self.heap.sort() # Simple sort for demonstration

    def pop(self):
        return self.heap.pop(0) if self.heap else None

h = Heap()
h.push(4)
h.push(1)
h.push(7)
print(h.pop()) # Output: 1

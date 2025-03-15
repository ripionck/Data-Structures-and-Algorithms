# Generate binary numbers from 1 to n

class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")


def generate_binary_numbers(n):
    result = []
    q = Queue()
    q.enqueue("1")

    for i in range(n):
        front = q.dequeue()
        result.append(front)

        q.enqueue(front + "0")
        q.enqueue(front + "1")

    return result


n = 10
binary_numbers = generate_binary_numbers(n)
print(f"Binary numbers from 1 to {n}:")
for i, num in enumerate(binary_numbers, 1):
    print(f"{i} : {num}")


"""
Time complexity: O(n)
Space complexity: O(n)
"""

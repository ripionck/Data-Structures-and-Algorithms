from collections import deque

dq = deque()

# Append elements
dq.append(10)
dq.append(20)
dq.appendleft(5)
print("Deque after appending:", dq)

# Pop elements
dq.pop()
dq.popleft()
print("Deque after popping:", dq)

# Extend the deque
dq.extend([30, 40, 50])
dq.extendleft([0, -10, -20])
print("Deque after extending:", dq)

# Rotate the deque
dq.rotate(1)
print("Deque after rotating right by 1:", dq)
dq.rotate(-1)
print("Deque after rotating left by 1:", dq)

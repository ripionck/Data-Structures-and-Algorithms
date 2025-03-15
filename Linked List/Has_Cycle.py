class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

# Approach 1 : using set
def has_cycle_set(head):
    visited = set()
    current = head
    while current:
        if current in visited:
            return True
        visited.add(current)
        current = current.next
    return False

# Approach 2: using slow and fast pointers
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False

def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head


head = create_linked_list([3, 2, 0, -4])
print(has_cycle(head))  
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
     
# approach 1: Two Passes
def middle_node(head):
    length = 0
    current = head
    while current:
        length += 1
        current = current.next
            
    middle = length // 2
    current = head
    for _ in range(middle):
        current = current.next
        
    return current

# approach 2: Slow and fast pointers
def middle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    return slow
        
        
def create_linked_list(values):
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head
    

head = create_linked_list([1,2,3,4,5,6])
print(middle(head))  
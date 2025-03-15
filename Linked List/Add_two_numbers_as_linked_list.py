class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        current = dummy
        carry = 0

        while l1 or l2 or carry:
            # Get values
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0

            # Calculate sum
            total = x + y + carry
            carry = total // 10
            digit = total % 10

            # Create new node
            current.next = ListNode(digit)
            current = current.next

            # Move to next nodes
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next


def create_linked_list(arr):
    dummy = ListNode(0)
    current = dummy
    for num in arr:
        current.next = ListNode(num)
        current = current.next
    return dummy.next


def print_linked_list(head):
    current = head
    result = []
    while current:
        result.append(str(current.val))
        current = current.next
    return ' -> '.join(result)


# Example usage
if __name__ == "__main__":
    # Create two linked lists
    l1 = create_linked_list([2, 4, 3])  # Represents 342
    l2 = create_linked_list([5, 6, 4])  # Represents 465

    solution = Solution()
    result = solution.addTwoNumbers(l1, l2)

    print("Number 1:", print_linked_list(l1))
    print("Number 2:", print_linked_list(l2))
    print("Sum:     ", print_linked_list(result))

    # Another example
    l3 = create_linked_list([9, 9, 9, 9])  # Represents 9999
    l4 = create_linked_list([9, 9, 9, 9, 9, 9])  # Represents 999999

    result2 = solution.addTwoNumbers(l3, l4)

    print("\nNumber 1:", print_linked_list(l3))
    print("Number 2:", print_linked_list(l4))
    print("Sum:     ", print_linked_list(result2))

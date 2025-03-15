class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        # Edge cases: empty list or k = 0
        if not head or not head.next or k == 0:
            return head

        # Find the length of the list and the last node
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1

        # Adjust k if it's larger than the length of the list
        k = k % length
        if k == 0:
            return head

        # Find the new last node (length - k - 1 steps from head)
        new_last = head
        for _ in range(length - k - 1):
            new_last = new_last.next

        # Rotate the list
        new_head = new_last.next
        new_last.next = None
        last.next = head

        return new_head


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
    # Create a linked list
    head = create_linked_list([1, 2, 3, 4, 5])

    solution = Solution()

    print("Original list:", print_linked_list(head))

    # Rotate by 2
    rotated = solution.rotateRight(head, 2)
    print("Rotated by 2:", print_linked_list(rotated))

    # Rotate by 7 (equivalent to rotating by 2)
    rotated = solution.rotateRight(head, 7)
    print("Rotated by 7:", print_linked_list(rotated))

    # Rotate by 0
    rotated = solution.rotateRight(head, 0)
    print("Rotated by 0:", print_linked_list(rotated))

    # Edge case: single node
    single_node = create_linked_list([1])
    rotated = solution.rotateRight(single_node, 1)
    print("Single node rotated by 1:", print_linked_list(rotated))

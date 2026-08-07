from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def delete_middle(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head

    node = head
    list_size = 0
    while node:
        list_size += 1
        node = node.next

    if list_size == 1:
        return None

    middle = list_size // 2
    node_index = 0
    node = head
    while node:
        if node_index == middle:
            previous_node.next = node.next
            return head

        previous_node = node
        node = node.next
        node_index += 1


# complexity O(N)
def delete_middle_second_approach(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return head

    if head.next is None:
        return None

    base_node = None
    slow_node = head
    fast_node = head

    while fast_node and fast_node.next:
        base_node = slow_node
        slow_node = slow_node.next
        fast_node = fast_node.next.next

    base_node.next = slow_node.next

    return head
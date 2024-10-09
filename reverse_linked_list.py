from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(self, head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return

    node = head
    previous_node = None

    while node:
        temp_node = node
        node = node.next
        temp_node.next = previous_node
        previous_node = temp_node

    return previous_node


'''
time complexity: O(N) - because to invert we have to visit every node at least once 
space complexity: O(N) - because if you make the inversion inline, we loose the reference a
nd we have to create a new list to return
'''



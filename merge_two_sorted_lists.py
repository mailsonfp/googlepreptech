from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_two_lists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    if list1 == None:
        return list2

    if list2 == None:
        return list1

    if list1.val > list2.val:
        temp = list1
        list1 = list2
        list2 = temp

    head = list1
    while (list1 != None and list2 != None):

        if list1.next == None:
            list1.next = list2
            return head

        if list1.val <= list2.val and list1.next.val >= list2.val:
            list2.next, list1.next, list2 = list1.next, list2, list2.next

        list1 = list1.next

    return head
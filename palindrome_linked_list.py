class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def is_palindrome_linked_list(head):
    is_palindrome = True

    array_linked_list_value = []

    if head.next is None:
        return is_palindrome

    while head:
        array_linked_list_value.append(head.val)
        head = head.next

    j = len(array_linked_list_value) - 1
    for i in range(len(array_linked_list_value)):
        if array_linked_list_value[i] != array_linked_list_value[j]:
            is_palindrome = False
            break

        j -= 1

    return is_palindrome


def is_palindrome_linked_list_dois(head):
    if head.next is None:
        return True

    first_node_value = None
    last_node_value = None
    is_mid_equal = True
    count = 0
    while head:
        if count == 0:
            first_node_value = head.val
        else:
            if head.next is None:
                last_node_value = head.val
            else:
                if head.val != head.next.val and head.next.next is not None:
                    is_mid_equal = False
        head = head.next
        count += 1

    return first_node_value == last_node_value and is_mid_equal


if __name__ == '__main__':
    new_node_4 = ListNode(1)
    new_node_3 = ListNode(2, new_node_4)
    new_node_2 = ListNode(2, new_node_3)
    new_node_1 = ListNode(1, new_node_2)

    print(is_palindrome_linked_list_dois(new_node_1))

    new_node_2 = ListNode(2)
    new_node_1 = ListNode(1, new_node_2)

    print(is_palindrome_linked_list_dois(new_node_1))
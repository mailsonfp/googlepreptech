class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


def get_decimal_value(head:ListNode):
    base_five_number = 0

    while head:
        base_five_number = 2*base_five_number + head.val
        head = head.next

    return base_five_number


if __name__ == '__main__':
    list_param = []

    new_node_3 = ListNode(1)
    new_node_2 = ListNode(0, new_node_3)
    new_node_1 = ListNode(1, new_node_2)

    number = get_decimal_value(new_node_1)

    print(number)
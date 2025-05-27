class MyLinkedList:

    def __init__(self):
        self.head = ListNode(0)
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1

        node = self.head.next
        for i in range(index):
            node = node.next

        return node.val

    def addAtHead(self, val: int) -> None:
        temp_node = self.head.next
        self.head.next = ListNode(val)
        self.head.next.next = temp_node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = self.head

        while node.next:
            node = node.next

        node.next = ListNode(val)
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return

        previous = self.head
        for i in range(index):
            previous = previous.next

        temp_node = previous.next
        previous.next = ListNode(val)
        previous.next.next = temp_node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return

        previous = self.head
        for _ in range(index):
            previous = previous.next

        temp_node = previous.next
        previous.next = temp_node.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
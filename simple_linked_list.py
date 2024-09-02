class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_head(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return

        previous = self.head
        while previous.next is not None:
            previous = previous.next

        previous.next = new_node

    def insert_after(self, data, position):
        new_node = Node(data)
        previous = self.head
        for i in range(position):
            if previous is None:
                return

            previous = previous.next

        new_node.next = previous.next
        previous.next = new_node

    def remove_end(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        previous = self.head
        while previous.next is not None:
            previous = previous.next

        previous.next = None

    def remove_position(self, position):
        previous = self.head
        for i in range(position):
            if previous is None:
                return
            previous = previous.next
        if previous.next is None:
            return

    def print_list(self):
        message_to_print = ""

        if self.head is None:
            message_to_print = "empty_list"
        else:
            previous = self.head
            message_to_print = str(previous.data)
            while previous.next is not None:
                previous = previous.next
                message_to_print += " - " + str(previous.data)

        print(message_to_print)


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.print_list()

    linked_list.insert_head(5)
    linked_list.print_list()

    linked_list.insert_after(10, 0)
    linked_list.print_list()

    linked_list.insert_after(25, 1)
    linked_list.print_list()

    linked_list.insert_after(35, 0)
    linked_list.print_list()

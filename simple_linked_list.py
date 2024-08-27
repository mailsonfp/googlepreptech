class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self, head):
        self.head = head

    def insertHead(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


if __name__ == '__main__':
    node = Node(5)
    print(node)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None and self.rear is None

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None

        temp = self.front()
        self.front = temp.next
        if self.front is None:
            self.rear = None

        return temp.data

    def front(self):
        if self.is_empty():
            return None

        return self.front.data


if __name__ == '__main__':
    queue = Queue()
    queue.enqueue(5)

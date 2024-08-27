class Stack:
    def __init__(self):  # constructor
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.pop()

    def top(self):
        if not self.is_empty():
            return self.items[-1]

        return None

    def is_empty(self):
        return len(self.items) == 0

    def print_stack(self):
        if self.is_empty():
            print("Empty stack")
            return

        for i in range(len(self.items)):
            print(self.items[i])


if __name__ == '__main__':
    stack = Stack()
    stack.push(5)
    stack.push(3)
    stack.print_stack()

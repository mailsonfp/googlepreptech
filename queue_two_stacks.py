# complexity o(n)
class QueueTwoStacks:
    def __init__(self):
        self.main_array = []
        self.shadow_array = []

    def push(self, element):
        for i in range(len(self.main_array)):
            self.shadow_array.append(self.main_array.pop())

        self.main_array.append(element)

        for i in range(len(self.shadow_array)):
            self.main_array.append(self.shadow_array.pop())

    def pop(self):
        if self.is_empty():
            return None
        return self.main_array.pop()

    def peek(self):
        if self.is_empty():
            return None
        temp = self.main_array.pop()
        self.main_array.append(temp)
        return temp

    def is_empty(self):
        return len(self.main_array) == 0

    def print(self):
        if self.is_empty():
            print("Empty Queue")
            return
        message = ""
        for i in range(len(self.main_array)):
            if message == "":
                message = message + "Fifo queue: " + str(self.main_array[i])
            else:
                message = message + " - " + str(self.main_array[i])

        print(message)


if __name__ == '__main__':
    fifo_queue = QueueTwoStacks()
    fifo_queue.push(0)
    fifo_queue.push(1)
    fifo_queue.push(2)
    fifo_queue.print()
    print(f"Pop: {fifo_queue.pop()}")
    fifo_queue.print()
    fifo_queue.push(5)
    print(f"Peek: {fifo_queue.peek()}")
    fifo_queue.print()

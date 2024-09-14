class MyStack:
    def __init__(self):
        self.main_queue = []
        self.shadow_queue = []

    def push(self, x: int) -> None:
        self.shadow_queue.append(x)
        for i in range(len(self.main_queue), 0, -1):
            self.shadow_queue.append(self.shadow_queue.pop())

        for i in range(len(self.shadow_queue)):
            self.main_queue.append(self.shadow_queue.pop())

    def pop(self) -> int:
        if self.empty():
            return -1

        return self.main_queue.pop()

    def top(self) -> int:
        if self.empty():
            return -1

        return self.main_queue[len(self.main_queue)-1]

    def empty(self) -> bool:
        return len(self.main_queue) == 0

    def print(self):
        if self.empty():
            print("Empty Queue")
            return
        message = ""
        for i in range(len(self.main_queue)):
            if message == "":
                message = message + "Fifo queue: " + str(self.main_queue[i])
            else:
                message = message + " - " + str(self.main_queue[i])

        print(message)


if __name__ == '__main__':
    obj = MyStack()
    obj.push(10)
    obj.push(15)
    obj.push(35)
    obj.print()
    param_2 = obj.pop()
    print(param_2)
    param_3 = obj.top()
    print(param_3)
    param_4 = obj.empty()
    print(param_4)

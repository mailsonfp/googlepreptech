class Stack:
    def __init__(self):  # constructor
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

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


def polish_notation(tokens):
    stack = Stack()
    for i in range(len(tokens)):
        if tokens[i] in ("+", "-", "*", "/"):
            right_number = int(stack.pop())
            left_number = int(stack.pop())
            result = 0
            if tokens[i] == "+":
                result = left_number + right_number
            elif tokens[i] == "-":
                result = left_number - right_number
            elif tokens[i] == "*":
                result = left_number * right_number
            elif tokens[i] == "/":
                result = int(left_number / right_number)

            stack.push(result)
        else:
            stack.push(tokens[i])

    return stack.pop()


if __name__ == '__main__':
    tokens = ["2", "1", "+", "3", "*"]
    print(polish_notation(tokens))

    tokens = ["4", "13", "5", "/", "+"]
    print(polish_notation(tokens))

    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
    print(polish_notation(tokens))

    tokens = ["18"]
    print(polish_notation(tokens))

    tokens = ["3", "-4", "+"]
    print(polish_notation(tokens))

    tokens = ["4", "-2", "/", "2", "-3", "-", "-"]
    print(polish_notation(tokens))
def polish_notation(tokens):
    if len(tokens) == 1:
        return tokens[0]

    stack = []
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
                result = int(left_number/right_number)

            stack.append(result)
        else:
            stack.append(tokens[i])

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
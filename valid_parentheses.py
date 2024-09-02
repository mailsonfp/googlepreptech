def is_valid_parenthesis(string_to_validate):
    stack = []

    for character in string_to_validate:
        if character in '([{':
            stack.append(character)
        else:
            if len(stack) == 0:
                return False
            else:
                if character == ")" and stack[-1] != "("\
                        or character == "]" and stack[-1] != "["\
                        or character == "}" and stack[-1] != "{":
                    return False

                stack.pop()

    return len(stack) == 0


if __name__ == '__main__':
    input_string = "()"
    print(is_valid_parenthesis(input_string))

    input_string = "()[]{}"
    print(is_valid_parenthesis(input_string))

    input_string = "(]"
    print(is_valid_parenthesis(input_string))

    input_string = "([])"
    print(is_valid_parenthesis(input_string))

    input_string = "([)]"
    print(is_valid_parenthesis(input_string))

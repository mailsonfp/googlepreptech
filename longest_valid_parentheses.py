def longest_valid_parenthesis(string_base):
    stack = [-1]

    max_length = 0

    for i, char in enumerate(string_base):
        if char == '(':
            stack.append(i)
        else:
            stack.pop()

            if stack:
                print(f"max_length: {max_length}")
                print(f"i: {i}")
                print(f"stack[-1]: {stack[-1]}")
                max_length = max(max_length, i - stack[-1])
            else:
                stack.append(i)

    return max_length


if __name__ == '__main__':
    base_str = '(()'
    print(f"baseStr: {base_str}")
    print(f"longest valid parenthesis: {longest_valid_parenthesis(base_str)}")

    base_str = ')()())'
    print(f"baseStr: {base_str}")
    print(f"longest valid parenthesis: {longest_valid_parenthesis(base_str)}")

    base_str = ''
    print(f"baseStr: {base_str}")
    print(f"longest valid parenthesis: {longest_valid_parenthesis(base_str)}")

    base_str = '))))'
    print(f"baseStr: {base_str}")
    print(f"longest valid parenthesis: {longest_valid_parenthesis(base_str)}")

    base_str = '(((('
    print(f"baseStr: {base_str}")
    print(f"longest valid parenthesis: {longest_valid_parenthesis(base_str)}")
from typing import List


def do_generate_parenthesis(current_return=None, quantity_open=0, quantity_close=0, n=0, return_array=None, max_parenthesis=0):
    if return_array is None:
        return_array = []

    if current_return is None:
        current_return = []

    if (quantity_open + quantity_close) == max_parenthesis:
        return_array.append(''.join(current_return))
        return

    if quantity_open < n:
        current_return.append("(")
        do_generate_parenthesis(current_return, quantity_open + 1, quantity_close, n, return_array, max_parenthesis)
        current_return.pop()

    if quantity_close < quantity_open:
        current_return.append(")")
        do_generate_parenthesis(current_return, quantity_open, quantity_close + 1, n, return_array, max_parenthesis)
        current_return.pop()


def generate_parenthesis(n: int) -> List[str]:
    return_array = []
    max_parenthesis = n * 2
    do_generate_parenthesis(["("], 1, 0, n, return_array, max_parenthesis)

    return return_array


if __name__ == '__main__':
    n_param = 3
    print(generate_parenthesis(n_param))
    n_param = 1
    print(generate_parenthesis(n_param))

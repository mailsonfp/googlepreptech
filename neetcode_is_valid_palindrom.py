import re


def is_palindrome(s: str) -> bool:
    s_aux = re.search(r'[A-Za-z]', s)

    left_index = 0
    right_index = len(s) - 1
    while left_index < right_index:
        if s[left_index].isalpha() and s[right_index].isalpha():
            if s[left_index] != s[right_index]:
                return False

        left_index += 1
        right_index -= 1

    return True


if __name__ == '__main__':
    s = "Was it a car or a cat I saw?"
    print(f"is_palindrome: {is_palindrome(s)}")

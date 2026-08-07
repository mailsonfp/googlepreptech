def count_deletions_to_anagram(string_a, string_b):
    letters = "abcdefghijklmnopqrstuvwxyz"
    frequency_string_a = {char: 0 for char in letters}
    frequency_string_b = {char: 0 for char in letters}

    for char in string_a:
        frequency_string_a[char] = frequency_string_a.get(char, 0) + 1

    for char in string_b:
        frequency_string_b[char] = frequency_string_b.get(char, 0) + 1

    return sum(abs(frequency_string_a[char] - frequency_string_b[char]) for char in letters)


# - Time Complexity: O(n + m)
# - Space Complexity: O(1)
if __name__ == '__main__':
    a = "abcd"
    b = "cdef"
    print(f"number of deletions for anagram: {count_deletions_to_anagram(a, b)}")

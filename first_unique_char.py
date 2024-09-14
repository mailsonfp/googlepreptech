def first_unique_char(s: str) -> int:
    dict_letters = dict()
    for letter in s:
        dict_letters[letter] = 1 + dict_letters.get(letter, 0)

    first_unique_letter = ""
    for key, val in dict_letters.items():
        if val == 1:
            first_unique_letter = key
            break

    if first_unique_letter == "":
        return -1

    return s.index(first_unique_letter)


if __name__ == '__main__':
    word = "leetcode"
    print(f"First unique char, position: {first_unique_char(word)}")

    word = "loveleetcode"
    print(f"First unique char, position: {first_unique_char(word)}")

    word = "aabb"
    print(f"First unique char, position: {first_unique_char(word)}")

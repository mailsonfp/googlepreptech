def is_vowel(letter):
    return letter in "AaEeIiOoUu"


# complexity O(n log n)
def sort_vowel(s):
    string_return = ""

    s_vowels = []

    for letter in s:
        if is_vowel(letter):
            s_vowels.append(letter)

    s_vowels.sort()

    j = 0
    for i in range(len(s)):
        if is_vowel(s[i]):
            string_return = string_return + s_vowels[j]
            j += 1
        else:
            string_return = string_return + s[i]

    return string_return


# complexity O(n)
def sort_vowel_approach(s):
    string_return = ""

    return string_return


if __name__ == '__main__':
    word = "lEetcOde"
    print(sort_vowel(word))

    word = "lYmpH"
    print(sort_vowel(word))

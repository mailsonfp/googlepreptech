# complexity: o(n²)
def is_isomorphic(s, t):
    if len(s) != len(t):
        return False

    map_s = []
    map_t = []

    for letter in s:
        map_t.append(s.index(letter))

    for letter in t:
        map_s.append(t.index(letter))

    return map_s == map_t


# complexity: o(n)
def is_isomorphic_approach_two(s, t):
    if len(s) != len(t):
        return False

    map_chars = dict()
    set_vals = set()

    for i in range(len(s)):
        s_char = s[i]
        t_char = t[i]
        if s[i] in map_chars:
            if map_chars[s_char] != t_char:
                return False
        else:
            if t_char in set_vals:
                return False
            map_chars[s_char] = t_char
            set_vals.add(t_char)

    return True


if __name__ == '__main__':
    word_1 = "egg"
    word_2 = "add"
    print(f"first approache: {is_isomorphic(word_1, word_2)}")
    print(f"second approache: {is_isomorphic_approach_two(word_1, word_2)}")

    word_1 = "foo"
    word_2 = "bar"
    print(f"first approache: {is_isomorphic(word_1, word_2)}")
    print(f"second approache: {is_isomorphic_approach_two(word_1, word_2)}")

    word_1 = "paper"
    word_2 = "title"
    print(f"first approache: {is_isomorphic(word_1, word_2)}")
    print(f"second approache: {is_isomorphic_approach_two(word_1, word_2)}")

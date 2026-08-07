def are_almost_equal(s1: str, s2: str) -> bool:
    if s1 == s2:
        return True

    position_1, position_2 = -1, -1
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            if position_1 == -1:
                position_1 = i
            elif position_2 == -1:
                position_2 = i
            else:
                return False

    return (position_1 == -1 and position_2 == -1) or (position_1 != -1 and position_2 != -1
                                                       and s1[position_1] == s2[position_2]
                                                       and s1[position_2] == s2[position_1])


if __name__ == '__main__':
    word1 = "bank"
    word2 = "kanb"
    print(f"Is possible with one swap? {are_almost_equal(word1, word2)}")

    word1 = "attack"
    word2 = "defend"
    print(f"Is possible with one swap? {are_almost_equal(word1, word2)}")

    word1 = "kelb"
    word2 = "kelb"
    print(f"Is possible with one swap? {are_almost_equal(word1, word2)}")

    word1 = "abcd"
    word2 = "dcba"
    print(f"Is possible with one swap? {are_almost_equal(word1, word2)}")

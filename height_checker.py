def height_checker(heights: [int]) -> int:
    heights_expected = heights[:]
    heights_expected.sort()
    count_unmatch = 0
    for i in range(len(heights)):
        if heights[i] != heights_expected[i]:
            count_unmatch += 1

    return count_unmatch


if __name__ == "__main__":
    array_param = [1, 1, 4, 2, 1, 3]
    print(f"heights unmatch: {height_checker(array_param)}")

    array_param = [5, 1, 2, 3, 4]
    print(f"heights unmatch: {height_checker(array_param)}")

    array_param = [1, 2, 3, 4, 5]
    print(f"heights unmatch: {height_checker(array_param)}")
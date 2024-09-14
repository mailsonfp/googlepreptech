def majority_element(nums) -> int:
    if len(nums) == 1:
        return nums[0]

    frequencies = ["X"] * (len(nums) + 1)
    count_dictionary = dict()

    for number in nums:
        count_dictionary[number] = 1 + count_dictionary.get(number, 0)

    for key, val in count_dictionary.items():
        frequencies[val] = key

    for i in range(len(frequencies)-1, 0, -1):
        if frequencies[i] != "X":
            return int(frequencies[i])


if __name__ == '__main__':
    array = [3, 2, 3]
    print(f"majority element: {majority_element(array)}")
    array = [2, 2, 1, 1, 1, 2, 2]
    print(f"majority element: {majority_element(array)}")
    array = [2, 2]
    print(f"majority element: {majority_element(array)}")
    array = [1000000000, 1000000000, -1000000000, -1000000000, -1000000000]
    print(f"majority element: {majority_element(array)}")
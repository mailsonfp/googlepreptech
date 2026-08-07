def top_k_frequent(nums, k):
    frequencies = [[] for _ in range(len(nums)+1)]
    count_dictionary = dict()

    for number in nums:
        count_dictionary[number] = 1 + count_dictionary.get(number, 0)

    for key, val in count_dictionary.items():
        frequencies[val].append(key)

    array_return = []
    for i in range(len(frequencies)-1, 0, -1):
        for number in frequencies[i]:
            array_return.append(number)
            if len(array_return) == k:
                return array_return

    return array_return


if __name__ == '__main__':
    array = [1, 1, 1, 2, 2, 3]
    top_k = 2
    print(top_k_frequent(array, top_k))

    array = [1]
    top_k = 1
    print(top_k_frequent(array, top_k))

    array = [-1, -1]
    top_k = 1
    print(top_k_frequent(array, top_k))

    array = [1, 2]
    top_k = 2
    print(top_k_frequent(array, top_k))

    array = [2, 2]
    top_k = 2
    print(top_k_frequent(array, top_k))

    array = [3, 0, 1, 0]
    top_k = 1
    print(top_k_frequent(array, top_k))

    array = [4, 1, -1, 2, -1, 2, 3]
    top_k = 2
    print(top_k_frequent(array, top_k))

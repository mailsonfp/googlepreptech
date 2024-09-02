def merge_sort(array_to_sort_1, array_to_sort_1_size, array_to_sort_2, array_to_sort_2_size):
    merged_array = []
    i, j = 0, 0
    while i < array_to_sort_1_size and j < array_to_sort_2_size:
        if array_to_sort_1[i] < array_to_sort_2[j]:
            merged_array.append(array_to_sort_1[i])
            i += 1
        else:
            merged_array.append(array_to_sort_2[j])
            j += 1
    while i < array_to_sort_1_size:
        merged_array.append(array_to_sort_1[i])
        i += 1
    while j < array_to_sort_2_size:
        merged_array.append(array_to_sort_2[j])
        j += 1

    for index in range(len(array_to_sort_1)):
        array_to_sort_1[index] = merged_array[index]


if __name__ == '__main__':
    array_1 = [1, 3, 8, 10, 43, 55, 79, 85, 0, 0, 0, 0, 0, 0]
    array_1_number_size = 8
    array_2 = [7, 14, 22, 33, 53, 74]
    array_2_number_size = 1
    print(f"Array to sort 1: {array_1}")
    print(f"Array to sort 2: {array_2}")
    merge_sort(array_1, array_1_number_size, array_2, array_2_number_size)
    print(f"Array sorted merge_sort: {array_1}")

    print('-' * 20)

    array_1 = [2, 0]
    array_1_number_size = 1
    array_2 = [1]
    array_2_number_size = 1
    print(f"Array to sort 1: {array_1}")
    print(f"Array to sort 2: {array_2}")
    merge_sort(array_1, array_1_number_size, array_2, array_2_number_size)
    print(f"Array sorted merge_sort: {array_1}")

    print('-' * 20)

    array_1 = [4, 5, 6, 0, 0, 0]
    array_1_number_size = 3
    array_2 = [1, 2, 3]
    array_2_number_size = 3
    print(f"Array to sort 1: {array_1}")
    print(f"Array to sort 2: {array_2}")
    merge_sort(array_1, array_1_number_size, array_2, array_2_number_size)
    print(f"Array sorted merge_sort: {array_1}")

    print('-' * 20)

    array_1 = [4, 0, 0, 0, 0, 0]
    array_1_number_size = 1
    array_2 = [1, 2, 3, 5, 6]
    array_2_number_size = 5
    print(f"Array to sort 1: {array_1}")
    print(f"Array to sort 2: {array_2}")
    merge_sort(array_1, array_1_number_size, array_2, array_2_number_size)
    print(f"Array sorted merge_sort: {array_1}")

# complexity: O(N²)
def selection_sort(array_to_sort):
    for i in range(len(array_to_sort)):
        for j in range(i + 1, len(array_to_sort)):
            if array_to_sort[j] < array_to_sort[i]:
                array_to_sort[i], array_to_sort[j] = array_to_sort[j], array_to_sort[i]

    return array_to_sort


# complexity: O(N²)
def buble_sort(array_to_sort):
    for i in range(len(array_to_sort)):
        any_swap = False
        for j in range(i):
            if array_to_sort[j] > array_to_sort[j + 1]:
                array_to_sort[j], array_to_sort[j + 1] = array_to_sort[j + 1], array_to_sort[j]
                any_swap = True

        if not any_swap:
            break

    return array_to_sort


# complexity: N log2 N
def merge_sort(array_to_sort):
    if len(array_to_sort) > 1:
        mid = len(array_to_sort) // 2
        array_to_sort_left_half, array_to_sort_right_half = array_to_sort[0:mid], array_to_sort[mid:]

        merge_sort(array_to_sort_left_half)
        merge_sort(array_to_sort_right_half)

        index_left, index_right, new_index = 0, 0, 0

        while index_left < len(array_to_sort_left_half) and index_right < len(array_to_sort_right_half):
            if array_to_sort_left_half[index_left] < array_to_sort_right_half[index_right]:
                array_to_sort[new_index] = array_to_sort_left_half[index_left]
                index_left += 1
            else:
                array_to_sort[new_index] = array_to_sort_right_half[index_right]
                index_right += 1
            new_index += 1

        while index_left < len(array_to_sort_left_half):
            array_to_sort[new_index] = array_to_sort_left_half[index_left]
            index_left += 1
            new_index += 1

        while index_right < len(array_to_sort_right_half):
            array_to_sort[new_index] = array_to_sort_right_half[index_right]
            index_right += 1
            new_index += 1


# complexity: N log2 N
def quick_sort(array_to_sort):
    len_array_to_sort = len(array_to_sort)
    if len_array_to_sort > 0:
        quick_sort_do_order(array_to_sort, 0, len_array_to_sort - 1)
    else:
        return []


def quick_sort_do_order(array_to_sort, left, right):
    if left < right:
        partition_index = partition(array_to_sort, left, right)
        quick_sort_do_order(array_to_sort, left, partition_index - 1)
        quick_sort_do_order(array_to_sort, partition_index + 1, right)


def partition(array_to_sort, left, right):
    pivot = array_to_sort[left]
    previous = left + 1
    after = right

    do_order = True
    while do_order:
        while previous <= after and array_to_sort[previous] <= pivot:
            previous += 1

        while after >= previous and array_to_sort[after] >= pivot:
            after -= 1

        if after < previous:
            do_order = False
        else:
            temp = array_to_sort[previous]
            array_to_sort[previous] = array_to_sort[after]
            array_to_sort[after] = temp

    temp = array_to_sort[left]
    array_to_sort[left] = array_to_sort[after]
    array_to_sort[after] = temp

    return after


def count_sort(array_to_sort):
    array_count = [0] * len(array_to_sort)

    for i in range(len(array_to_sort)):
        array_count[array_to_sort[i]] += 1

    index_sort = 0

    for i in range(len(array_count)):
        if array_count[i] > 0:
            for j in range(array_count[i], 0, -1):
                array_to_sort[index_sort] = i
                index_sort += 1
                array_count[i] -= 1


if __name__ == '__main__':
    array = [85, 55, 42, 3, 8, 10, 79, 1]
    print(f"Array to sort: {array}")
    print(f"Array sorted selection_sort: {selection_sort(array)}")

    print('-' * 20)

    array = [85, 55, 42, 3, 8, 10, 79, 1]
    print(f"Array to sort: {array}")
    print(f"Array sorted buble_sort: {selection_sort(array)}")

    print('-' * 20)

    array = [85, 55, 42, 3, 8, 10, 79, 1]
    print(f"Array to sort: {array}")
    merge_sort(array)
    print(f"Array sorted merge_sort: {array}")

    print('-' * 20)

    array = [85, 55, 42, 3, 8, 10, 79, 1]
    print(f"Array to sort: {array}")
    quick_sort(array)
    print(f"Array sorted quick_sort: {array}")

    print('-' * 20)

    array = [3, 1, 2, 1, 1, 3]
    print(f"Array to sort: {array}")
    count_sort(array)
    print(f"Array sorted count_sort: {array}")

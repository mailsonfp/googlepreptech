def merge_sort(nums1, m, nums2, n):
    if m == 0:
        for i in range(n):
            nums1[i] = nums2[i]

        return
    elif m == 1:
        for i in range(n):
            if nums1[i] > nums2[i]:
                nums1[i + 1] = nums1[i]
                nums1[i] = nums2[i]
            else:
                nums1[i + 1] = nums2[i]

        return

    if n == 1:
        zero_position = m
        for i in range(m - 1, 0, -1):
            if nums1[i] > nums2[n - 1]:
                temp = nums1[i]
                nums1[i] = nums1[zero_position]
                nums1[i + 1] = temp

                zero_position = i
            else:
                break

        nums1[zero_position] = nums2[0]

        return

    end_index = len(nums1) - 1
    while m > 0 and n > 0:
        if nums2[n - 1] >= nums1[m - 1]:
            nums1[end_index] = nums2[n - 1]
            n -= 1
        else:
            nums1[end_index] = nums1[m - 1]
            m -= 1

        end_index -= 1

    if len(nums2) == n:
        for end_index in range(n):
            nums1[end_index] = nums2[end_index]
            end_index += 1
    else:
        while n > 0:
            nums1[end_index] = nums2[n]
            n -= 1
            end_index -= 1


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

    print('-' * 20)

    array_1 = [1, 2, 4, 5, 6, 0]
    array_1_number_size = 5
    array_2 = [3]
    array_2_number_size = 1
    print(f"Array to sort 1: {array_1}")
    print(f"Array to sort 2: {array_2}")
    merge_sort(array_1, array_1_number_size, array_2, array_2_number_size)
    print(f"Array sorted merge_sort: {array_1}")

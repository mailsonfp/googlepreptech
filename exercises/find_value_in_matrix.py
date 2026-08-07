def find_value_in_matrix(base_matrix, target):
    for line in base_matrix:
        if find_target(line[0:len(line)], target):
            return True

    return False


def find_target(line, target):
    index_found = binary_search(line, target)

    return index_found >= 0


def binary_search(base_array, target):
    index = -1
    left = 0
    right = len(base_array) - 1

    while left <= right:
        mid = (left + right) // 2

        if base_array[mid] == target:
            index = mid
            break
        elif base_array[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index


# time complexity: O(n log m).
# space complexity: O(n log m)
if __name__ == '__main__':
    matrix = [[1, 2, 4], [4, 5, 6], [7, 8, 9]]
    target_to_find = 8
    print(f"exist target: {find_value_in_matrix(matrix,target_to_find)}")
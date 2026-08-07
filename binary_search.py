def search(nums, target):
    index = -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            index = mid
            break
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return index


def solution_sum(array):
    mid = len(array) // 2
    print(f'len: {len(array) // 2}')

    sum_one = 1
    sum_two = 1
    # for i in range(mid+1):
    #     print(f'array[i]: {array[i]}')
    #     sum_one *= array[i]
    #
    #     print(f'array[mid+i]: {array[mid+i]}')
    #     sum_two *= array[mid+i]
    line = [0] * len(array)
    for i in range(array):
        for j in range(len(array), -1, -1):
            line.append(array[i] * array[j] * array[j-1])

    print(line)

    return 0


if __name__ == '__main__':
    nums = [-10, 1, -10, 3, 2]
    print(solution_sum(nums))

    nums = [1, 2, 3, 4, 5]
    print(solution_sum(nums))

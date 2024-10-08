import math


# complexity O(nlogn)
def sorted_squares_direct(nums: [int]) -> [int]:
    for i in range(len(nums)):
        nums[i] = int(math.pow(nums[i], 2))

    nums.sort()

    return nums


# complexity o(N)
def sorted_squares_two_pointers(nums: [int]) -> [int]:
    array_return = [0] * len(nums)

    left_index, right_index = 0, len(nums) - 1

    for i in range(len(array_return), 0, -1):
        if abs(nums[left_index]) >= abs(nums[right_index]):
            array_return[i] = int(math.pow(nums[left_index], 2))
            left_index += 1
        else:
            array_return[i] = int(math.pow(nums[right_index], 2))
            right_index -= 1

    return array_return


if __name__ == "__main__":
    array_param = [-4, -1, 0, 3, 10]
    print(f"array param: {array_param}")
    print(f"square of arrays direct: {sorted_squares_direct(array_param)}")
    array_param = [-4, -1, 0, 3, 10]
    print(f"square of arrays two_pointers: {sorted_squares_direct(array_param)}")

    print('-' * 20)
    print(f"array param: {array_param}")
    array_param = [-7, -3, 2, 3, 11]
    print(f"square of arrays direct: {sorted_squares_direct(array_param)}")
    array_param = [-7, -3, 2, 3, 11]
    print(f"square of arrays two_pointers: {sorted_squares_direct(array_param)}")

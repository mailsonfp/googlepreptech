from typing import List


def backtracking(target, i, result, count, nums):
    if i == len(nums):
        if result == target:
            count += 1

        return count

    temp = 0
    backtracking(target, i + 1, result + nums[i], count, nums)
    backtracking(target, i + 1, result - nums[i], count, nums)

    return count


def find_target_sum_ways(nums, target):
    result = 0
    count = 0
    return backtracking(target, 0, 0, count, nums)


if __name__ == '__main__':
    nums_param = [1, 1, 1, 1, 1]
    target_param = 3
    print(f"ways to targetSum: {find_target_sum_ways(nums_param, target_param)}")
    nums_param = [1]
    print(f"ways to targetSum: {find_target_sum_ways(nums_param, target_param)}")

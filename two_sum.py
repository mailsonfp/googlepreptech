def two_sum(nums, target):
    pairs = {}

    for i in range(len(nums)):
        if target - nums[i] in pairs:
            return [i, pairs[target - nums[i]]]

        pairs[nums[i]] = i


if __name__ == '__main__':
    array = [2, 7, 11, 15]
    target_param = 9
    print(f"numbers to achieve target: {two_sum(array, target_param)}")
    array = [3, 2, 4]
    target_param = 6
    print(f"numbers to achieve target: {two_sum(array, target_param)}")
    array = [3, 3]
    target_param = 6
    print(f"numbers to achieve target: {two_sum(array, target_param)}")
    array = [3, 2, 3]
    target_param = 6
    print(f"numbers to achieve target: {two_sum(array, target_param)}")
    array = [2, 5, 5, 11]
    target_param = 10
    print(f"numbers to achieve target: {two_sum(array, target_param)}")
    array = [-3, 4, 3, 90]
    target_param = 0
    print(f"numbers to achieve target: {two_sum(array, target_param)}")
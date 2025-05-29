def pair_sum_set(base_array, target):
    output = []
    num_set = set(base_array)

    for i in base_array:
        if (i - target) in num_set:
            output.append((i, i - target))

    return output


def pair_sum_brute_force(base_array, target):
    output = []

    for i in range(len(base_array)):
        for j in range(i+1, len(base_array)):
            if abs(base_array[i] - base_array[j]) == target:
                output.append((base_array[i], base_array[j]))

    return output


if __name__ == '__main__':
    array = [1, 5, 3, 4, 2]
    target_to_find = 2
    print(f"positions with difference equals target: {pair_sum_set(array, target_to_find)}")
    print(f"positions with difference equals target brute force: {pair_sum_brute_force(array, target_to_find)}")
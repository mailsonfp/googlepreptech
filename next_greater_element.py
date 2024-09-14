# O(n²)
def next_greater_element_approach_one(nums1, nums2):
    array_position = [0] * len(nums1)
    array_return = [-1] * len(nums1)

    for nums_1_index in range(len(nums1)):
        for num_2_index in range(len(nums2)):
            if nums1[nums_1_index] == nums2[num_2_index]:
                array_position[nums_1_index] = num_2_index
                break

    for position_index in range(len(array_position)):
        for position in range(array_position[position_index] + 1, len(nums2)):
            if nums2[position] > nums1[position_index]:
                array_return[position_index] = nums2[position]
                break
            else:
                array_return[position_index] = -1

    return array_return


def next_greater_element_approach_two(nums1, nums2):
    array_return = [-1] * len(nums1)
    return "to do melhorar complexidade"


if __name__ == '__main__':
    first_array = [4, 1, 2]
    second_array = [1, 3, 4, 2]
    print(next_greater_element_approach_one(first_array,second_array))
    print(next_greater_element_approach_two(first_array, second_array))

    first_array = [2, 4]
    second_array = [1, 2, 3, 4]
    print(next_greater_element_approach_one(first_array, second_array))
    print(next_greater_element_approach_two(first_array, second_array))

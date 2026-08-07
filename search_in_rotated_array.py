
def partition_rotated(array_to_sort, left, right, pivot):
    previous = left + 1
    after = right

    do_order = True
    while do_order:
        while previous >= after and array_to_sort[previous] >= pivot:
            previous += 1

        while after <= previous and array_to_sort[after] <= pivot:
            after -= 1

        if after > previous:
            do_order = False
        else:
            temp = array_to_sort[previous]
            array_to_sort[previous] = array_to_sort[after]
            array_to_sort[after] = temp

    temp = array_to_sort[left]
    array_to_sort[left] = array_to_sort[after]
    array_to_sort[after] = temp

    return after


def do_rotation(nums, left, right, pivot):
    if left < right:
        partition_index = partition_rotated(nums, left, right, pivot)
        do_rotation(nums, left, partition_index - 1, pivot)
        do_rotation(nums, partition_index + 1, right, pivot)


if __name__ == "__main__":
    print("todo")


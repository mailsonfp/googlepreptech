import heapq
import random


def find_kth_largest_sort(nums, k):
    nums.sort()
    for i in range(len(nums), 0, -1):
        if k == 0:
            return nums[i]

        k -= 1


def partition(nums, left_index, right_index, pivot_index):
    pivot = nums[pivot_index]
    nums[pivot_index], nums[right_index] = nums[right_index], nums[pivot_index]
    stored_index = left_index
    for i in range(left_index, right_index):
        if nums[i] < pivot:
            nums[i], nums[stored_index] = nums[stored_index], nums[i]
            stored_index += 1

    nums[right_index], nums[stored_index] = nums[stored_index], nums[right_index]

    return stored_index


def find_kth_largest_quick_selection(nums, k):
    left_index, right_index = 0, len(nums) - 1
    while True:
        pivot_index = random.randint(left_index, right_index)
        new_pivot_index = partition(nums, left_index, right_index, pivot_index)
        if new_pivot_index == len(nums) - k:
            return nums[new_pivot_index]
        elif new_pivot_index > len(nums) - k:
            right_index = new_pivot_index - 1
        else:
            left_index = new_pivot_index + 1


def find_kth_largest_heap_solution(nums, k):
    heap = nums[:k]
    heapq.heapify(heap)

    for number in nums[k:]:
        if number > heap[0]:
            heapq.heappop(heap)
            heapq.heappush(heap, number)

    return heap[0]


if __name__ == "__main__":
    array_param = [3, 2, 1, 5, 6, 4]
    k_param = 2
    print(f"kth largest element with sort: {find_kth_largest_sort(array_param,k_param)}")
    print(f"kth largest element with quick_selection: {find_kth_largest_quick_selection(array_param, k_param)}")
    print(f"kth largest element with heap: {find_kth_largest_heap_solution(array_param, k_param)}")
    array_param = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k_param = 4
    print(f"kth largest element with sort: {find_kth_largest_sort(array_param, k_param)}")
    print(f"kth largest element with quick_selection: {find_kth_largest_quick_selection(array_param, k_param)}")
    print(f"kth largest element with heap: {find_kth_largest_heap_solution(array_param, k_param)}")

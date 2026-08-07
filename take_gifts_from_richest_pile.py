import heapq
import math
from typing import List
from queue import PriorityQueue


def pick_gifts(gifts: List[int], k: int) -> int:
    priority_array = PriorityQueue()
    gifts.sort(reverse=True)
    priority = 0
    for number in gifts:
        priority_array.put(number)
        priority += 1

    for i in range(k):
        max_number = priority_array.get()
        max_number = int(math.sqrt(max_number[1]))
        priority_array.put(max_number)
        priority += 1

    count_return = 0
    while priority_array:
        count_return += priority_array.get()[1]

    return count_return


def pick_gifts_heap(gifts: List[int], k: int) -> int:
    heap_array = []
    for number in gifts:
        heapq.heappush(heap_array, number)

    for i in range(k):
        max_number = heapq.heappop(heap_array)
        max_number = int(math.sqrt(max_number))
        heapq.heappush(heap_array, max_number)

    count_return = 0
    for i in range(len(gifts)):
        count_return += gifts[i]

    return count_return


if __name__ == '__main__':
    gifts_param = [25, 64, 9, 4, 100]
    k_param = 4
    print(f"number left gifts: {pick_gifts(gifts_param, k_param)}")
    #print(f"number left gifts: {pick_gifts_heap(gifts_param, k_param)}")

def combine_generate(n, k, start=1, partial_return_array=[], combinations_array=[]):
    if len(partial_return_array) == k:
        combinations_array.append([x for x in partial_return_array])
        return

    for currentStart in range(start, n + 1):
        partial_return_array.append(currentStart)

        combine_generate(n, k, currentStart + 1, partial_return_array, combinations_array)

        partial_return_array.pop()

    return combinations_array


def combine(n: int, k: int):
    return combine_generate(n, k, 1, [], [])


# complexity O(K∗C(N,K)) ; memory O(K∗C(N,K))
if __name__ == '__main__':
    n_parm = 4
    k_param = 2
    combinations_array = combine(n_parm, k_param)
    print(f"Combinations_array params n={n_parm} k={k_param} = {combine(n_parm, k_param)}")
    n_parm = 1
    k_param = 1
    combined_array = combine(n_parm, k_param)
    print(f"Combinations_array params n={n_parm} k={k_param} = {combine(n_parm, k_param)}")
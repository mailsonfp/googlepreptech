def min_swaps(grid):
    zeroes = [0]*len(grid) #array with zeroes count
    for i in range(len(grid)):
        for j in range(len(grid[i])-1, -1, -1): #counting zeroes at end of row
            if grid[i][j] == 1:
                break
            zeroes[i] += 1

    required_zeroes = len(grid)-1 #required zeroes at each row
    swap_count = 0

    for i in range(len(zeroes)):
        found_required_zeroes = False
        for j in range(i, len(zeroes)):
            if zeroes[j] >= required_zeroes:
                found_required_zeroes = True
                break

            for k in range(j, i, -1):
                zeroes[k], zeroes[k-1] = zeroes[k-1], zeroes[k]
                swap_count += 1

            required_zeroes -= 1

        if not found_required_zeroes:
            return -1

    return swap_count


def minimum_swaps(grid_to_swap):
    grid_size = len(grid_to_swap)

    zeros_count = [0] * grid_size

    for i in range(grid_size):
        for j in range(len(grid_to_swap[i])-1, -1, -1):
            if grid_to_swap[i][j] == 1:
                break

            zeros_count[i] += 1

    required_zeros = grid_size - 1
    swap_count = 0

    for i in range(len(zeros_count)):
        found_required_zeros = False
        for j in range(i, len(zeros_count)):
            if zeros_count[j] >= required_zeros:
                found_required_zeros = True
                break

            for k in range(j, i, -1):
                zeros_count[k], zeros_count[k-1] = zeros_count[k-1], zeros_count[k]
                swap_count += 1

            required_zeros -= 1

        if not found_required_zeros:
            return -1

    return swap_count


if __name__ == '__main__':
    grid = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
    print(grid)
    print(min_swaps(grid))

    print('-' * 20)

    grid = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]
    print(grid)
    print(minimum_swaps(grid))

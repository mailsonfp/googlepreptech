class Node:
    def __init__(self, val, nex=None):
        self.val = val
        self.nex = None


def minimum_swaps(grid):
    n = len(grid)

    head = c_tail = Node(-1)  # dummy node
    for row in grid:
        c = 0
        for v in reversed(row):
            if v: break
            c += 1
        new_node = Node(c)
        c_tail.nex = new_node
        c_tail = new_node

    moves = 0
    for c in range(n - 1, 0, -1):

        i = 0
        c_node = head
        while c_node.nex:
            if c_node.nex.val >= c:
                moves += i
                c_node.nex = c_node.nex.nex
                break
            i += 1
            c_node = c_node.nex
        else:
            return -1

    return moves


if __name__ == '__main__':
    grid_to_swap = [[0, 0, 1], [1, 1, 0], [1, 0, 0]]
    print(f"Number of moves: {minimum_swaps(grid_to_swap)}")

    grid_to_swap = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0]]
    print(f"Number of moves: {minimum_swaps(grid_to_swap)}")

    grid_to_swap = [[1, 0, 0], [1, 1, 0], [1, 1, 1]]
    print(f"Number of moves: {minimum_swaps(grid_to_swap)}")
 
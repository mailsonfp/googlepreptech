class Node:
    def __init__(self, val: int = None, children=None):
        self.val = val
        self.children = children


def max_depth(root):
    return max_depth_aux(root)


def max_depth_aux(root):
    if not root:
        return 0

    if len(root.children) == 0:
        return 1

    max_depth = 0
    for child in root.children:
        depth = max_depth_aux(child)
        max_depth = max(max_depth, depth)

    return max_depth + 1


if __name__ == '__main__':
    root_param = [1, None, 3, 2, 4, None, 5, 6]
    node_tree = Node(3,[5, 6])
    node_two = Node(2)
    node_four = Node(5)
    print(f"Tree graph: {max_depth(root_param)}")

    root_param = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None, None, 14]
    print(f"Tree graph: {max_depth(root_param)}")

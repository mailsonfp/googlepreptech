class TreeNode:
    def __init__(self, val, children=None):
        if children is None:
            children = []

        self.value = val
        self.children = children


def max_depth_auth(root):
    if not root:
        return 0

    if len(root.children) == 0:
        return 1

    max_depth_aux = 0
    for child in root.children:
        depth = max_depth_auth(child)
        max_depth_aux = max(max_depth_aux, depth)

    return max_depth_aux + 1


def max_depth(root):
    return max_depth_auth(root)


if __name__ == '__main__':
    tree_node_six = TreeNode(6)
    tree_node_five = TreeNode(5)
    tree_node_tree = TreeNode(3, [tree_node_five, tree_node_five])

    tree_node_two = TreeNode(2)

    tree_node_four = TreeNode(4)

    tree_node_root = TreeNode(1, [tree_node_tree, tree_node_two, tree_node_four])

    print(f"Max Depth of Tree: {max_depth(tree_node_root)}")

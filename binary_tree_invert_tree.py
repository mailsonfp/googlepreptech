class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def print_tree(node):
    if node:
        print(f"node_val: {node.value}")
        if node.left:
            print_tree(node.left)
        else:
            print("no left node")

        if node.right:
            print_tree(node.right)
        else:
            print("no right node")
    else:
        print("empty")


def invert_tree(root):
    if not root:
        return None
    root.left, root.right = root.right, root.left

    invert_tree(root.left)
    invert_tree(root.right)

    return root


if __name__ == '__main__':
    tree_node_one = TreeNode(1)
    tree_node_three = TreeNode(3)
    tree_node_two = TreeNode(2,tree_node_one, tree_node_three)
    tree_node_six = TreeNode(6)
    tree_node_nine = TreeNode(9)
    tree_node_seven = TreeNode(7, tree_node_six, tree_node_nine)
    tree_node_head = TreeNode(4, tree_node_two, tree_node_seven)
    print_tree(tree_node_head)
    invert_tree(tree_node_head)
    print("***----***"*5)
    print_tree(tree_node_head)

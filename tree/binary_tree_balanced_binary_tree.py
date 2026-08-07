# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def get_height(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return 1

    height_left = get_height(root.left) + 1
    height_right = get_height(root.right) + 1

    return max(height_left, height_right)


def insert_into_bst(root, val):
    if not root:
        return TreeNode(val)

    if val > root.value:
        root.right = insert_into_bst(root.right, val)
    else:
        root.left = insert_into_bst(root.left, val)

    return root


def is_balanced(root: TreeNode) -> bool:
    if not root:
        return True

    if not root.left and not root.right:
        return True

    height_left = get_height(root.left)
    height_right = get_height(root.right)

    if abs(height_left - height_right) <= 1:
        return is_balanced(root.left) and is_balanced(root.right)

    return False


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


if __name__ == '__main__':
    tree_node_head = insert_into_bst(None, 3)
    insert_into_bst(tree_node_head, 2)
    insert_into_bst(tree_node_head, 7)
    insert_into_bst(tree_node_head, 1)
    insert_into_bst(tree_node_head, 3)
    print_tree(tree_node_head)
    tree = TreeNode()
    # [3,9,20,null,null,15,7]
    # [1, 2, 2, 3, 3, null, null, 4, 4]
    # []

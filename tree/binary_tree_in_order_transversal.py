class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def transverse(root, result):
    if not root:
        return result

    transverse(root.left, result)
    result.append(root.value)
    transverse(root.right, result)


def in_order_traversal(root):
    """
    :type root: TreeNode
    :rtype: List[int]
    """

    result = []
    transverse(root, result)

    return result


# complexity O(N)
if __name__ == '__main__':
    treeNode = TreeNode()
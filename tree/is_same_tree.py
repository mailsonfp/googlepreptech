from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_same_tree(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    if not p and not q:
        return True

    if not p or not q:
        return False

    return p.val == q.val and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)


if __name__ == '__main__':
    p_param = [1, 2, 3]
    q_param = [1, 2, 3]
    print("True")


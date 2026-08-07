from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(self, root, target, partial, results):
    if not root:
        return

    partial.append(root.val)

    if not root.left and not root.right and sum(partial) == target:
        results.append(list(partial))

    self.traverse(root.left, target, partial, results)
    self.traverse(root.right, target, partial, results)
    partial.pop()


def path_sum(self, root: Optional[TreeNode], target_sum: int) -> List[List[int]]:
    results = []
    self.traverse(root, target_sum, [], results)
    return results


if __name__ == '__main__':
    root_param = [5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1]
    # print [[5,4,11,2],[5,8,4,5]]
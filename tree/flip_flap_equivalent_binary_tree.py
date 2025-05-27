''''
Approach 2: Iterative DFS (using a Stack)
Intuition

While a recursive method is intuitive, it can lead to issues such as stack overflow for very deep trees.

By using an iterative DFS(Depth-first search) approach with a stack, we can simulate the recursive process while maintaining control over the stack size. The idea is to push pairs of nodes onto the stack and evaluate their equivalence in a structured manner, ultimately determining if the trees can be made equivalent through flips.
Algorithm

    Define a helper function checkNodeValues to verify if two nodes should be considered equivalent:
        If both node1 and node2 are nullptr, return true.
        If both nodes are not nullptr and their values match, return true.
        Otherwise, return false.
    In the flipEquiv main function:
        Initialize a stack s to store pairs of nodes (node1, node2) from root1 and root2.
        Push the root nodes of both trees onto the stack.
    While the stack is not empty:
        Pop the top pair of nodes from the stack.
        If both node1 and node2 are nullptr, continue to the next iteration.
        If only one of the nodes is nullptr, return false (trees are not equivalent).
        If the values of node1 and node2 do not match, return false.
        Check both configurations for equivalence:
            If the left child of node1 matches the left child of node2 and the right child of node1 matches the right child of node2, push these pairs onto the stack for further examination.
            If the left child of node1 matches the right child of node2 and the right child of node1 matches the left child of node2, push these pairs onto the stack.
        If neither configuration is satisfied, return false.
    If the stack is emptied without returning false, return true, indicating that the two trees are flip equivalent.

'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkNodeValues(self, node1, node2):
        if not node1 and not node2:
            return True

        if node1 and node2 and node1.val == node2.val:
            return True

        return False

    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        stack_node_aux = []
        stack_node_aux.append((root1, root2))

        while stack_node_aux:
            node_1, node_2 = stack_node_aux.pop()

            if not node_1 and not node_2:
                continue

            if not node_1 or not node_2:
                return False

            if node_1.val != node_2.val:
                return False

            if self.checkNodeValues(
                    node_1.left, node_2.left
            ) and self.checkNodeValues(node_1.right, node_2.right):
                stack_node_aux.append((node_1.left, node_2.left))
                stack_node_aux.append((node_1.right, node_2.right))
            elif self.checkNodeValues(
                    node_1.left, node_2.right
            ) and self.checkNodeValues(node_1.right, node_2.left):
                stack_node_aux.append((node_1.left, node_2.right))
                stack_node_aux.append((node_1.right, node_2.left))
            else:
                return False

        return True
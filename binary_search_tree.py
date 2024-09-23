class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def insert(root, val):
    if not root:
        return TreeNode(val)

    if val > root.value:
        root.right = insert(root.right, val)
    else:
        root.left = insert(root.left, val)

    return root


def delete(root, key):
    if not root:
        return None

    if root.value > key:
        root.left = delete(root.left, key)
    elif root.value < key:
        root.right = delete(root.right, key)
    else:  # root.value == key
        if not root.left:
            return root.right

        if not root.right:
            return root.left

        it = root.right
        while it.left:
            it = it.left

        root.value, it.value = it.value, root.value
        root.right = delete(root.right, it.value)

    return root


def search(root, val):
    if not root:
        return None

    if val == root.value:
        return root

    if val > root.value:
        return search(root.right, val)
    else:
        return search(root.left, val)


def is_valid_aux(root, minimum_value, maximum_value):
    if not root:
        return True

    if root.left and root.left.value >= root.value:
        return False

    if root.right and root.right.value <= root.value:
        return False

    if root.value <= minimum_value or maximum_value <= root.value:
        return False

    return is_valid_aux(root.left, minimum_value, root.value) and is_valid_aux(root.right, root.value, maximum_value)


def is_valid(root):
    return is_valid_aux(root, float('-inf'), float('inf'))


def lowest_common_ancestor(root, p, q):
    if (p.value <= root.value <= q.value) or (p.value >= root.value >= q.value):
        return root

    if root.value >= p.value and root.value >= q.value:
        return lowest_common_ancestor(root.left, p, q)
    else:
        return lowest_common_ancestor(root.right, p, q)


def search_successor(root, base_node):
    successor = None
    while root:
        if root.value > base_node.value:
            successor = root
            root = root.left
        else:
            root = root.right

    return successor


def search_predecessor(root, base_node):
    predecessor = None
    while root:
        if root.value < base_node.value:
            predecessor = root
            root = root.left
        else:
            root = root.right

    return predecessor


def in_order(root, base_array):
    if not root:
        return

    in_order(root.left, base_array)
    base_array.append(root.value)
    in_order(root.right, base_array)


def do_balance(base_array, left, right):
    if left > right:
        return None

    mid = (left + right) // 2
    root = TreeNode(base_array[mid])
    root.left = do_balance(base_array, left, mid - 1)
    root.right = do_balance(base_array, mid + 1, right)

    return root


# complexity O(N)
def balance(root):
    base_array = []
    in_order(root, base_array)
    return do_balance(base_array, 0, len(base_array) - 1)


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
    root_tree_node = insert(None, 4)
    print_tree(root_tree_node)
    root_tree_node = insert(root_tree_node, 7)
    root_tree_node = insert(root_tree_node, 2)
    root_tree_node = insert(root_tree_node, 3)
    root_tree_node = insert(root_tree_node, 1)
    root_tree_node = insert(root_tree_node, 9)
    root_tree_node = insert(root_tree_node, 10)
    root_tree_node = insert(root_tree_node, 5)
    root_tree_node = insert(root_tree_node, 6)
    root_tree_node = insert(root_tree_node, 12)
    root_tree_node = insert(root_tree_node, 13)
    root_tree_node = insert(root_tree_node, 15)
    root_tree_node = insert(root_tree_node, 16)
    root_tree_node = insert(root_tree_node, 17)
    root_tree_node = insert(root_tree_node, 20)
    print_tree(root_tree_node)
    search_val = search(root_tree_node, 1)
    if search_val:
        print(f"Search val 1, resul: {search_val.value}")
    else:
        print("Not found")
    search_val = search(root_tree_node, 9)
    if search_val:
        print(f"Search val 9, resul: {search_val.value}")
    else:
        print("9 Not found")

    print(f"is valid bsb {is_valid(root_tree_node)}")
    tree_node_seven = search(root_tree_node, 7)
    tree_node_two = search(root_tree_node, 2)
    print(
        f"lowest common ancestor of bsb {lowest_common_ancestor(root_tree_node, tree_node_seven, tree_node_two).value}")
    print(f"Successor node of number 7 is numer: {search_successor(root_tree_node, tree_node_seven).value}")
    print(f"Predecessor node of number 2 is number: {search_successor(root_tree_node, tree_node_two).value}")
    print("*-----*", 8)
    root_tree_node = delete(root_tree_node, 7)
    print_tree(root_tree_node)
    print("*-----*", 8)
    root_tree_node = balance(root_tree_node)
    print_tree(root_tree_node)
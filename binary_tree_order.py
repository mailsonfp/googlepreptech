def do_order(root, order):
    array_return = []

    if order == "INORDER":
        do_in_order(root, array_return)
    elif order == "PREORDER":
        do_pre_order(root, array_return)
    elif order == "POSTORDER":
        do_post_order(root, array_return)

    return array_return


def do_in_order(root, base_array):
    if not root:
        return

    do_in_order(root.left, base_array)

    base_array.append(root.value)

    do_in_order(root.right, base_array)


def do_pre_order(root, base_array):
    if not root:
        return

    base_array.append(root.value)

    do_pre_order(root.left, base_array)
    do_pre_order(root.right, base_array)


def do_post_order(root, base_array):
    if not root:
        return

    do_post_order(root.left, base_array)
    do_post_order(root.right, base_array)

    base_array.append(root.value)

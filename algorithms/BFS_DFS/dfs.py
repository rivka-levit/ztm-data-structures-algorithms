from data_structures.trees.binary_search_tree import Node, BinarySearchTree


def in_order_traverse(node: Node, visited: list = None) -> None | list:
    if not node:
        return
    if visited is None:
        visited = list()
    in_order_traverse(node.left, visited)
    visited.append(node.value)
    in_order_traverse(node.right, visited)
    return visited


def pre_order_traverse(node: Node, visited: list = None) -> None | list:
    if not node:
        return
    if visited is None:
        visited = list()
    visited.append(node.value)
    pre_order_traverse(node.left, visited)
    pre_order_traverse(node.right, visited)
    return visited


def post_order_traverse(node: Node, visited: list = None) -> None | list:
    if not node:
        return
    if visited is None:
        visited = list()
    post_order_traverse(node.left, visited)
    post_order_traverse(node.right, visited)
    visited.append(node.value)
    return visited


if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree.insert(9)
    my_tree.insert(4)
    my_tree.insert(6)
    my_tree.insert(20)
    my_tree.insert(170)
    my_tree.insert(15)
    my_tree.insert(1)

    print(post_order_traverse(my_tree.root))
    print(pre_order_traverse(my_tree.root))
    print(in_order_traverse(my_tree.root))

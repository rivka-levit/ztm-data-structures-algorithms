from data_structures.trees.binary_search_tree import Node, BinarySearchTree


def in_order_traverse(node: Node, visited: list) -> None:
    if not node:
        return
    in_order_traverse(node.left, visited)
    visited.append(node.value)
    in_order_traverse(node.right, visited)


def pre_order_traverse(node: Node, visited: list) -> None:
    if not node:
        return
    visited.append(node.value)
    pre_order_traverse(node.left, visited)
    pre_order_traverse(node.right, visited)


def post_order_traverse():
    pass


if __name__ == '__main__':
    my_tree = BinarySearchTree()
    my_tree.insert(9)
    my_tree.insert(4)
    my_tree.insert(6)
    my_tree.insert(20)
    my_tree.insert(170)
    my_tree.insert(15)
    my_tree.insert(1)

    results = list()
    pre_order_traverse(my_tree.root, results)
    print(results)

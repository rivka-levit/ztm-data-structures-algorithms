from data_structures.trees.binary_search_tree import BinarySearchTree
from collections import deque


def bfs_iterative(bs_tree: BinarySearchTree) -> list:
    results = list()
    que = deque()

    current = bs_tree.root
    que.append(current)

    while que:
        current = que.popleft()
        results.append(current.value)
        if current.left:
            que.append(current.left)
        if current.right:
            que.append(current.right)

    return results


my_tree = BinarySearchTree()
my_tree.insert(9)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(20)
my_tree.insert(170)
my_tree.insert(15)
my_tree.insert(1)

print(bfs_iterative(my_tree))

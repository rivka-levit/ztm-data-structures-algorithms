from data_structures.trees.binary_search_tree import Node, BinarySearchTree
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


def bfs_recursive(node: Node, q: deque, results: list) -> list:
    # Base case
    if not node:
        return results

    # Node value to results list, it`s children to the queue
    results.append(node.value)
    if node.left:
        q.append(node.left)
    if node.right:
        q.append(node.right)

    # Get the next node form the queue
    try:
        next_node = q.popleft()
    except IndexError:
        next_node = None

    return bfs_recursive(next_node, q, results)


my_tree = BinarySearchTree()
my_tree.insert(9)
my_tree.insert(4)
my_tree.insert(6)
my_tree.insert(20)
my_tree.insert(170)
my_tree.insert(15)
my_tree.insert(1)

queue = deque()
visited = list()

print(bfs_iterative(my_tree))
print(bfs_recursive(my_tree.root, queue, visited))

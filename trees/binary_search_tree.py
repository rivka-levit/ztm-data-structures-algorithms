import json


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.value)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __str__(self):
        if not self.root:
            return '{Empty}'

        def traverse(node: Node):
            tree = dict()
            tree['value'] = node.value
            if node.left:
                tree['left'] = traverse(node.left)
            if node.right:
                tree['right'] = traverse(node.right)
            return tree

        return json.dumps(traverse(self.root))

    def __repr__(self):
        return self.__str__()

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            return True
        temp = self.root
        while temp:
            if value == temp.value:
                return False
            if value > temp.value:
                if not temp.right:
                    temp.right = new_node
                    return True
                temp = temp.right
            else:
                if not temp.left:
                    temp.left = new_node
                    return True
                temp = temp.left

    def lookup(self, value):
        if not self.root:
            return None
        temp = self.root
        while temp:
            if value == temp.value:
                return temp
            if value > temp.value:
                temp = temp.right
            else:
                temp = temp.left
        return None

    def remove(self, value):
        if not self.root:
            return False
        if self.root.value == value:
            self.root = None
            return True
        current = self.root
        while current:
            parent = current
            if value > current.value:
                current = current.right
            elif value < current.value:
                current = current.left
            else:
                # Option 1: No right child
                if not current.right:
                    if parent.right == current:
                        parent.right = current.left
                    elif parent.left == current:
                        parent.left = current.left
                    return True

                # Option 2: Right child that doesn't have a left child
                if not current.right.left:
                    current.right.left = current.left
                    if parent.right == current:
                        parent.right = current.right
                    elif parent.left == current:
                        parent.left = current.right
                    return True

                # Option 3: Right child that has a left child
                temp = current.right
                while temp.left:
                    parent = temp
                    temp = temp.left
                current.value, temp.value = temp.value, current.value
                if temp.right:
                    parent.left = temp.right
                else:
                    parent.left = None
                return True


my_little_tree = BinarySearchTree()
my_little_tree.insert(10)
my_little_tree.insert(5)
my_little_tree.insert(20)
my_little_tree.insert(8)
my_little_tree.insert(18)
my_little_tree.insert(28)
my_little_tree.insert(25)
my_little_tree.insert(30)
print(my_little_tree)
my_little_tree.remove(20)
print(my_little_tree)


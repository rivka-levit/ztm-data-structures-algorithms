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


my_tree = BinarySearchTree()
my_tree.insert(10)
my_tree.insert(5)
my_tree.insert(20)
my_tree.insert(8)
my_tree.insert(18)
print(my_tree.lookup(28))
my_tree.insert(28)
print(my_tree.lookup(28))

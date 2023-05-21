class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_ll(self):
        temp = self.head
        print('[ll--> ', end='')
        while temp:
            print(temp.value, end=' ')
            temp = temp.next
        print('<--ll]')

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def __traverse_to_index(self, index):
        """
        Returns the node on certain index in the list
        :param index: int
        :return : Node
        """
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def insert(self, index, value):
        # Check input
        if index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        # Check if list is not empty
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        # Insert the node inside the list
        leader = self.__traverse_to_index(index-1)
        new_node.next = leader.next
        leader.next = new_node
        self.length += 1
        return True


my_linked_list = LinkedList(10)
my_linked_list.append(5)
my_linked_list.append(16)
my_linked_list.print_ll()

my_linked_list.prepend(1)
my_linked_list.print_ll()
my_linked_list.insert(2, 3)
my_linked_list.print_ll()
print('LL length:', my_linked_list.length)

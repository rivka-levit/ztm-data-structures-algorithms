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

    def remove(self, index):
        # Check input
        if any((self.length == 0, index >= self.length, index < 0)):
            return False

        # Remove the first node
        if index == 0:
            self.head = self.head.next

        # Remove inside or at the end
        else:
            temp = self.__traverse_to_index(index-1)
            if self.tail == temp.next:
                self.tail = temp
            temp.next = temp.next.next

        self.length -= 1
        return True

    def reverse(self):
        if self.length == 0 or self.length == 1:
            return True
        if self.length == 2:
            self.tail.next = self.head
            self.head.next = None
            self.head, self.tail = self.tail, self.head
            return True

        # Pointers to handle the references
        before = self.head
        after = self.head.next

        # Reset all the references
        while after:
            current = after
            after = current.next
            current.next = before
            before = current

        # Update head and tail pointers
        self.head, self.tail = self.tail, self.head

        # Reference the tail
        self.tail.next = None
        return True


my_linked_list = LinkedList(1)
my_linked_list.append(10)
my_linked_list.append(16)
my_linked_list.append(88)
my_linked_list.print_ll()
my_linked_list.reverse()
my_linked_list.print_ll()

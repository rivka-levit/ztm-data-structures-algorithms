class DoubleNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = DoubleNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def __str__(self):
        temp = self.head
        result_string = '[ '
        while temp:
            result_string += str(temp.value) + ' '
            temp = temp.next
        return result_string + ']'

    def append(self, value):
        new_node = DoubleNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        new_node = DoubleNode(value)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    def __traverse_forward(self, index):
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def __traverse_backward(self, index):
        temp = self.tail
        for _ in range(abs(index)-1):
            temp = temp.prev
        return temp

    def insert(self, index, value):
        # Check input
        if index == self.length or index == -1:
            return self.append(value)
        if index == 0 or index + self.length == -1:
            return self.prepend(value)
        if abs(index) > self.length:
            return False

        new_node = DoubleNode(value)

        # Check if list is not empty
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            self.length += 1
            return True

        if index < 0:
            current = self.__traverse_backward(index)
            new_node.next = current.next
            current.next.prev = new_node
            new_node.prev = current
            current.next = new_node
        else:
            current = self.__traverse_forward(index)
            new_node.next = current
            new_node.prev = current.prev
            current.prev.next = new_node
            current.prev = new_node

        self.length += 1
        return True

    def remove(self, index):
        # Check input
        if self.length == 0 or index >= self.length:
            return False
        if index < 0 and abs(index) > self.length:
            return False

        # Remove the first node
        if index == 0 or index < 0 and abs(index) == self.length:
            self.head = self.head.next
            self.head.prev = None

        # Remove inside or at the end
        else:
            if index < 0:
                temp = self.__traverse_backward(index)
            else:
                temp = self.__traverse_forward(index)
            if self.tail == temp:
                self.tail = temp.prev
                self.tail.next = None
            else:
                temp.prev.next = temp.next
                temp.next.prev = temp.prev

        self.length -= 1
        return True

    def reverse(self):
        if self.length == 0 or self.length == 1:
            return True

        temp = self.tail

        # Reverse pointers
        while temp:
            temp.next, temp.prev = temp.prev, temp.next
            temp = temp.next

        # Change head and tail
        self.head, self.tail = self.tail, self.head

        return True


my_doubly_list = DoublyLinkedList(1)
my_doubly_list.append(5)
my_doubly_list.append(8)
print(my_doubly_list)
my_doubly_list.insert(-4, 77)
print(my_doubly_list)
my_doubly_list.prepend(7)
my_doubly_list.prepend(10)
print(my_doubly_list)
my_doubly_list.insert(-2, 99)
print(my_doubly_list)
my_doubly_list.insert(1, 68)
print(my_doubly_list)
my_doubly_list.remove(0)
print(my_doubly_list)
my_doubly_list.remove(-1)
print(my_doubly_list)
my_doubly_list.remove(-3)
print(my_doubly_list)
my_doubly_list.reverse()
print(my_doubly_list)

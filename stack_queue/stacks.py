class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        temp = self.top
        result_string = 'TOP\n'
        while temp:
            result_string += f'{temp.value}\n'
            temp = temp.next
        return result_string + 'BOTTOM'

    def is_empty(self):
        return True if self.length == 0 else False

    def peek(self):
        if self.is_empty():
            return None
        return self.top

    def push(self, value):
        new_node = Node(value)

        if self.is_empty():
            self.top = new_node
            self.bottom = new_node
        else:
            new_node.next = self.top
            self.top = new_node

        self.length += 1

    def pop(self):
        if self.is_empty():
            return None

        current = self.top

        if self.length == 1:
            self.top = None
            self.bottom = None
        else:
            self.top = current.next
            current.next = None

        self.length -= 1
        return current


my_stack = Stack()
my_stack.push(5)
my_stack.push(8)
my_stack.push(1)
print(my_stack)
print(my_stack.peek())
print(my_stack.pop())
print(my_stack)

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def __str__(self):
        temp = self.top
        result_string = 'TOP\n\\|/\n'
        while temp:
            result_string += f'{temp.value}\n'
            temp = temp.next
        return result_string + '/|\\\nBOTTOM'

    def is_empty(self):
        return self.length == 0

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
my_stack.push('Google')
my_stack.push('Udemy')
my_stack.push('Discord')
print(my_stack)
print()
print(my_stack.peek())
print(my_stack.pop())
print()
print(my_stack)

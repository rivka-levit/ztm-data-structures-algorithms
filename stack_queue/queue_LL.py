class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class MyQueue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        result_list = list()
        temp = self.first
        while temp:
            result_list.append(str(temp.value))
            temp = temp.next
        return f'[Q-- {", ".join(result_list)} --Q]'

    def is_empty(self):
        return self.length == 0

    def peek(self):
        return self.first

    def enqueue(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def deque(self):
        if self.is_empty():
            return None
        temp = self.first
        self.first = self.first.next
        self.length -= 1
        return temp


q = MyQueue()
q.enqueue('Matt')
q.enqueue('Frank')
q.enqueue('Pavel')
q.enqueue('Samir')
print(q)
print(q.peek())
print(q.deque())
print(q)
print(q.deque())
print(q)


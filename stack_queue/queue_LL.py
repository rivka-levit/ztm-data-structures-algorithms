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

    def is_empty(self) -> bool:
        """
        Return boolean value whether the list is empty or not.
        """
        return self.length == 0

    def peek(self) -> Node:
        """
        Return the first node without removing it
        from the queue.
        """
        return self.first

    def enqueue(self, value) -> None:
        """
        Takes a value from the input, creates a new
        node and appends it to the end of the queue.
        """
        new_node = Node(value)
        if self.is_empty():
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1

    def deque(self) -> Node | None:
        """
        Removes the first node in queue and returns it.
        """
        if self.is_empty():
            return None
        temp = self.first
        if self.length == 1:
            self.last = None
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


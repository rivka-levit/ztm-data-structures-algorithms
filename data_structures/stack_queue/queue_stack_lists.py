class MyQueueStack:
    def __init__(self):
        self.enq = list()
        self.deq = list()

    def __str__(self):
        if not self.enq:
            while self.deq:
                self.enq.append(self.deq.pop())
        return str(self.enq)

    def is_empty(self):
        return not self.enq and not self.deq

    def enqueue(self, value):
        if not self.enq:
            while self.deq:
                self.enq.append(self.deq.pop())
        self.enq.append(value)

    def dequeue(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        return self.deq.pop()

    def peek(self):
        if not self.deq:
            while self.enq:
                self.deq.append(self.enq.pop())
        return self.deq[-1] if not self.is_empty() else None


my_queue = MyQueueStack()
print(my_queue.peek())
my_queue.enqueue('Joy')
print(my_queue)
my_queue.enqueue('Matt')
print(my_queue)
my_queue.enqueue('Pavel')
print(my_queue)
print(my_queue.peek())
my_queue.dequeue()
print(my_queue)
my_queue.dequeue()
print(my_queue)
my_queue.dequeue()
print(my_queue)
my_queue.peek()

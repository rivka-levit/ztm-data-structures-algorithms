from stack_LL import Stack


class MyQueueStack:
    def __init__(self):
        self.data_main = Stack()
        self.data_helper = Stack()

    def push(self, value):
        self.data_main.push(value)

    def peek(self):
        while self.data_main:
            self.data_helper.push(self.data_main.pop())

        temp = self.data_helper.peek()

        while self.data_helper:
            self.data_main.push(self.data_helper.pop())

        return temp

    def pop(self):
        while self.data_main:
            self.data_helper.push(self.data_main.pop())

        temp = self.data_helper.pop()

        while self.data_helper:
            self.data_main.push(self.data_helper.pop())

        return temp

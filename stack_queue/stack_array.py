class StackArray:
    def __init__(self):
        self.data = list()

    def peek(self):
        if not self.data:
            return None
        return self.data[-1]

    def push(self, value):
        self.data.append(value)

    def pop(self):
        return self.data.pop()

import sys
class MinStack:

    def __init__(self):
        self.stack = []
        self.minimum = sys.maxsize

    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.minimum:
            self.minimum = val
        return self.stack

    def pop(self) -> None:
        if len(self.stack) > 0:
            top = self.stack[-1]
            self.stack.pop()
            if top == self.minimum:
                m = sys.maxsize
                for i in self.stack:
                    if i < m:
                        m = i
                self.minimum = m
        return self.stack

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minimum

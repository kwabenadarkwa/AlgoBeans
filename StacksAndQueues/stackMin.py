# INFO:
# Question Name: Stack Min
# How would you design a stack which, in addition to push and pop, has a function min
# which returns the minimum element? Push, pop and min should all operate in 0(1) time.

import math


class StackWithMin:
    def __init__(self):
        self.stack = []
        self.min_stack = []
        self.min = math.inf

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, value):
        if value <= self.min:
            self.min = value
            self.min_stack.append(value)
        self.stack.append(value)

    def view_min(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        else:
            return self.min

    def pop(self):
        if self.is_empty():
            raise Exception("The stack is empty")
        else:
            pop_value = self.stack[-1]
            if self.min_stack[-1] == self.stack[-1]:
                self.min = self.min_stack[-2] if len(self.min_stack) > 1 else math.inf
                self.min_stack.pop()
            self.stack.pop()
        return pop_value

    def peek(self):
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise Exception("The stack is empty please")


if __name__ == "__main__":
    stack = StackWithMin()
    stack.push(0)
    stack.push(1)
    stack.push(0)
    print(stack.view_min())
    stack.pop()
    print(stack.view_min())

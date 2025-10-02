from typing import  Union, Self

class ListNode:
    def __init__(self,value = 0):
        self.value = value
        self.next:Union[None,Self] = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self,value):
        current_top = ListNode(value)
        current_top.next = self.top
        self.top = current_top

    def pop(self):
        if self.top:
            self.top = self.top.next if self.top.next else None

    def peek(self):
        return self.top.value if self.top else None

    def is_empty(self):
        return self.top is None

if __name__ == "__main__":
    stack = Stack()
    stack.push(1)
    stack.push(3)
    stack.push(4)
    print(stack.peek())
    stack.pop()
    print(stack.peek())

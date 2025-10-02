# INFO:
# Sort Stack
# Write a program to sort a stack such that the smallest items are on the top. You can use
# an additional temporary stack, but you may not copy the elements into any other data structure
# (such as an array). The stack supports the following operations: push, pop, peek, and is Empty.

import math
from typing import Optional, Self


class Node:
    def __init__(self, value=0):
        self.value = value
        self.front: Optional[Self] = None
        self.back: Optional[Self] = None


class Stack:
    def __init__(self):
        self.size = 0
        self.top: Optional[Node] = None

    def is_empty(self) -> bool:
        return self.size == 0

    def peek(self) -> int:
        if not self.top:
            raise Exception("the stack is empty")
        else:
            return self.top.value 

    def push(self, value) -> None:
        if self.size != 0:
            previous_top: Node = self.top
            current_top = Node(value)
            current_top.back = previous_top
            self.top = current_top
            self.top.back = previous_top
            previous_top.front = self.top
        else:
            self.top = Node(value)

        self.size += 1

    def pop(self) -> int:
        if self.size == 0:
            raise Exception("the stack is empty")
        pop_value = self.top.value
        self.top = self.top.back
        self.size -= 1
        return pop_value


def print_stack(stack: Stack) -> None:
    """Print the contents of the stack from top to bottom."""
    if stack.is_empty():
        print("Stack is empty")
        return

    current = stack.top
    elements = []
    while current:
        elements.append(str(current.value))
        current = current.back

    print("Stack (top to bottom):", " -> ".join(elements))


def sort(stack: Stack) -> Stack:
    temp_stack = Stack()
    final_sorted_stack = Stack()
    max = -math.inf

    while not stack.is_empty():
        old_max = max
        old_max_met = False
        max = -math.inf

        while not stack.is_empty():
            popped_value = stack.pop()
            if popped_value == old_max and old_max_met is False:
                old_max_met = True
                continue
            elif popped_value >= max:
                max = popped_value
            temp_stack.push(popped_value)

        if(max != -math.inf):
            final_sorted_stack.push(max)

        old_max = max
        old_max_met = False
        max = -math.inf
        while not temp_stack.is_empty():
            popped_value = temp_stack.pop()
            if popped_value == old_max and old_max_met is False:
                old_max_met = True
                continue
            elif popped_value >= max:
                max = popped_value
            stack.push(popped_value)

        if(max != -math.inf):
            final_sorted_stack.push(max)

    # remove any value that's equal to -inf

    return final_sorted_stack


def sort_stack(s1: Stack) -> Stack:
    final_sorted_stack = Stack()  # final sorted stack
    temp_stack = Stack()  # buffer stack

    while not s1.is_empty():
        # Step 1: Find min in s1
        min_val = math.inf
        while not s1.is_empty():
            val = s1.pop()
            if val < min_val:
                min_val = val
            temp_stack.push(val)

        # Step 2: Move back to s1, skipping one occurrence of min
        min_skipped = False
        while not temp_stack.is_empty():
            val = temp_stack.pop()
            if val == min_val and not min_skipped:
                # skip this occurrence of min
                min_skipped = True
            else:
                s1.push(val)

        # Step 3: Push the min onto s2
        final_sorted_stack.push(min_val)

    return final_sorted_stack


def optimized_sort(stack:Stack):
    temp_stack = Stack()

    while not stack.is_empty():
        temp = stack.pop()
        while not temp_stack.is_empty() and temp_stack.peek() > temp :
            stack.push(temp_stack.pop())
        temp_stack.push(temp)

    while not temp_stack.is_empty():
        stack.push(temp_stack.pop())


if __name__ == "__main__":
    stack = Stack()
    stack.push(6)
    stack.push(2)
    stack.push(4)
    stack.push(5)
    stack.push(10)
    stack.push(115)
    stack.push(1)
    stack.push(100000)
    print("this is supposed to be the memory location of the stac",stack)
    print_stack(stack)
    optimized_sort(stack)
    print("this is supposed to be the memory location of the stac",stack)
    print_stack(stack)

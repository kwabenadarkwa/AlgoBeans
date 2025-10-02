#INFO:
#Iplement a MyQueue class which implements a queue using two stacks.
from typing import Optional, Self


class Node:
    def __init__(self,value):
        self.value = value
        self.front:Optional[Self] = None
        self.back:Optional[Self] = None

class Stack:
    def __init__(self):
        self.size = 0
        self.top:Optional[Node] = None

    def is_empty(self)->bool:
        return self.size == 0

    def push(self,value)->None:
        if self.size != 0:
            previous_top:Node = self.top
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

class MyQueue:
    def __init__(self):
        self.push_stack = Stack()
        self.pop_stack  = Stack()

    def enqueue(self,value):
        self.push_stack.push(value)


    def dequeue(self):
        if self.pop_stack.is_empty():
            if self.push_stack.is_empty():
                raise Exception("Queue is empty")
            else:
                self.move_from_push_stack()
                dequeue_value = self.pop_stack.pop()
        else:
            dequeue_value = self.pop_stack.pop()
        return dequeue_value

    def move_from_push_stack(self):
        current_top = self.push_stack.pop()
        while current_top: 
            self.pop_stack.push(current_top)
            if not self.push_stack.is_empty():
                current_top = self.push_stack.pop()
            else:
                break




if __name__ == "__main__":
    queue = MyQueue()
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    print(queue.dequeue())
    print(queue.dequeue())



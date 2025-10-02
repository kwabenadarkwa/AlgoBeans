from typing import  Union, Self

class QueueNode:
    def __init__(self,value = 0):
        self.value = value
        self.next:Union[None,Self] = None

class Queue:
    def __init__(self):
        self.head:Union[None,QueueNode] = None
        self.tail:Union[None,QueueNode] = None

    def is_empty(self):
        return self.head is None

    def add(self,value):
        insert_node = QueueNode(value)
        if self.tail is None:
            self.head = insert_node
            self.tail = insert_node
        else:
            self.tail.next = insert_node
            self.tail = insert_node

    def remove(self)->Union[None,QueueNode]:
        if self.head is None:
            return None
        else:
            new_top = self.head.next
            previous_top = self.head
            self.head = new_top
            if self.head is None:
                self.tail = None
            return previous_top

    def peek(self)->Union[None,QueueNode]:
        return self.head if not self.is_empty() else None



if __name__ == "__main__":
    stack = Queue()
    stack.add(1)
    stack.add(3)
    stack.add(4)
    stack.remove()
    stack.add(5)
    stack.remove()
    stack.remove()
    print(stack.peek().value)

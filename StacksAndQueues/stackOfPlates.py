# INFO:
# Stack of Plates: Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
# Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
# threshold Implement a data structure SetOfStacks that mimics this, setofstacks should be
# composed of several stacks and should create a new stack once the previous one exceeds capacity.
# SetOfStacks.push() and SetOfStacks.pop() should behave identically to a single stack
# (that is, pop () should return the same values as it would if there were just a single stack).
# FOLLOW UP
# Implement a function popAt (int index) which performs a pop operation on a specific sub-stack.


#could be solved this way but I think this technique involves too much hacking
from typing import List, Optional, Self


class SetOfStacksUnconventional:
    def __init__(self, init_max_stack_count):
        self.max_stack_count = init_max_stack_count
        # INFO: this size value doesn't track when popAT() has been called
        #in the case when that's been called the internal stack size helps us to know there to start
        #popping from in conjunction with the size
        self.size = 0
        self.current_internal_stack_count = 1
        first_stack = [0] * self.max_stack_count
        self.internal_stack_sizes = []
        self.internal_stack_sizes.append(0)
        self.set_of_stacks = []
        self.set_of_stacks.append(first_stack)

    def push(self, value):
        if self.size < self.max_stack_count:
            self.internal_stack_sizes[0] += 1
            self.set_of_stacks[0][self.size] = value
        elif self.size % self.max_stack_count == 0 and self.size >= self.max_stack_count:
            new_stack = [0] * self.max_stack_count
            new_stack[0] = value
            self.set_of_stacks.append(new_stack)
            self.internal_stack_sizes.append(1)
            self.current_internal_stack_count += 1
        else:
            internal_stack_to_target = self.current_internal_stack_count - 1
            index_in_internal_stack = self.size % self.max_stack_count
            self.internal_stack_sizes[internal_stack_to_target] += 1
            self.set_of_stacks[internal_stack_to_target][
                index_in_internal_stack
            ] = value
        print(self.set_of_stacks)
        print("internal stack size",self.internal_stack_sizes)
        self.size += 1


    def pop(self):
        if self.size == 0:
            raise Exception("There is nothing in the stack")
        else:
            if self.size <= self.max_stack_count:
                pop_value = self.set_of_stacks[0][self.size - 1]
                self.set_of_stacks[0][self.size - 1] = 0
            else:
                internal_stack_to_target = self.current_internal_stack_count - 1
                index_in_internal_stack = (self.size % self.max_stack_count) - 1
                if (
                    self.size % self.max_stack_count == 1
                    and self.size > self.max_stack_count
                ):
                    pop_value = self.set_of_stacks[internal_stack_to_target][0]
                    self.set_of_stacks.pop()
                    self.current_internal_stack_count -= 1
                else:
                    pop_value = self.set_of_stacks[internal_stack_to_target][
                        index_in_internal_stack 
                    ]
                    self.set_of_stacks[internal_stack_to_target][
                        index_in_internal_stack 
                    ] = 0

            self.size -= 1
        print(self.set_of_stacks)
        print("this is the pop value",pop_value)
        return pop_value

#INFO: the structures method from cracking the coding interview
#so they created a stack data structure that is made of several nodes to create the stack 
# then they created a the node data structure that is housed in those stacks

class Node: 
    def __init__(self,value:int):
        self.value:int = value
        self.above:Optional[Self] = None
        self.below:Optional[Self] = None


class Stack: 
    def __init__(self,capacity):
        self.capacity = capacity
        self.top:Optional[Node] = None
        self.bottom:Optional[Node] = None
        self.size = 0

    def is_full(self) -> bool:
        return self.size == self.capacity

    def is_empty(self) -> bool:
        return self.size == 0 

    def _join(self,above:Node,below:Node) -> None:
        if below is not None:
            below.above = above
        if above is not None: 
            above.below = below

    def push(self,value) -> bool:
        if self.size >= self.capacity: 
            return False

        self.size += 1
        n = Node(value)

        if self.size == 1: 
            self.bottom = n

        self._join(n,self.top)#type: ignore
        self.top = n
        return True

    #INFO:I think when using it they already check if it is empty before calling hence why the check isn't done here
    # I'm going to add it in mine anyway
    def pop(self) -> int:
        if self.is_empty():
            raise Exception("there is nothing to pop")
        t = self.top
        self.top = self.top.below #type:ignore
        self.size -= 1
        return t.value#type:ignore

    def remove_bottom(self) -> int: 
        bottom = self.bottom
        self.bottom = self.bottom.top#type:ignore
        self.size -= 1
        return bottom.value#type:ignore

class SetOfStacks:
    def __init__(self,capacity:int):
        self.capacity:int = capacity
        self.stacks:List[Stack] = []

    def push(self,value)->None:
        last_stack = self.get_last_stack()
        if last_stack and not last_stack.is_full(): 
            last_stack.push(value)
        else:
            new_stack = Stack(self.capacity)
            new_stack.push(value)
            self.stacks.append(new_stack)

    def get_last_stack(self)->Optional[Stack]:
        if len(self.stacks) == 0: 
            return None
        return self.stacks[-1]
    
    def pop(self)->int:
        last = self.get_last_stack()
        if not last:
            raise Exception("Stack is empty")
        v = last.pop()
        if last.is_empty():
            self.stacks.pop()
        return v
    # 
    # def is_empty(self)->bool:
    #     return len(self.stacks) == 0
    # 
    #version from book
    def is_empty(self)->bool:
        last = self.get_last_stack()
        return last is None or last.is_empty()
        
    def pop_at(self,index:int)->int:
        return self.left_shift(index,True)


    def left_shift(self,index:int, remove_top: bool) -> int:
        stack = self.stacks[index]
        removed_item = 0
        if remove_top: removed_item = stack.pop()
        else: removed_item = stack.remove_bottom()

        if stack.is_empty():
            self.stacks.remove(stack)

        elif len(self.stacks) > index + 1: 
            v = self.left_shift(index+1, False)
            stack.push(v)

        return removed_item

    def print_stacks(self) -> None:
        """Print all stacks with their elements in a readable format"""
        if not self.stacks:
            print("SetOfStacks is empty")
            return

        for i, stack in enumerate(self.stacks):
            elements = []
            current = stack.top
            while current:
                elements.append(str(current.value))
                current = current.below

            if elements:
                print(f"Stack {i}: [top] {' -> '.join(elements)} [bottom]")
            else:
                print(f"Stack {i}: [empty]")


if __name__ == "__main__":
    stack = SetOfStacks(3)
    stack.push(1)
    stack.print_stacks()
    stack.push(2)
    stack.print_stacks()
    stack.push(3)
    stack.print_stacks()
    stack.push(4)
    stack.print_stacks()
    stack.push(5)
    stack.print_stacks()
    stack.pop()
    stack.print_stacks()
    stack.pop()
    stack.print_stacks()
    stack.pop()
    stack.print_stacks()

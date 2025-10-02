# INFO:
# Three in One: Describe how you could use a single array to implement three stacks.

# TripleStack tripleStack = new TripleStack();
# // push(stackId, value)
# tripleStack.push(1, 50);
# tripleStack.push(2, 100);
# tripleStack.push(1, 100);
# tripleStack.push(3, 150);
# // peek(stackId)
# tripleStack.peek(1);  // returns 100
# tripleStack.peek(2);  // returns 100
# tripleStack.peek(3); // returns 150
# // pop(stackId)
# tripleStack.pop(1); // returns 100
# tripleStack.pop(1); // returns 50
# tripleStack.pop(2); // returns 100
# tripleStack.pop(3); // returns 150


# INFO: fixed approach division
# implement push, pop, peek, is Empty, isFull and indexOfTop
from typing import Optional


class TripleStack:
    _number_of_stacks = 3

    def __init__(self, stack_size):
        self.values = [0] * stack_size * self._number_of_stacks
        self.current_sizes = [0] * self._number_of_stacks
        self.stack_limit = stack_size

    def push(self, select_stack, value):
        if 0 < select_stack <= self._number_of_stacks:
            if self.is_full(select_stack):
                raise OverflowError("The stack is full")
            else:
                self.values[self.index_of_top(select_stack) + 1] = value
                self._increase_stack_size(select_stack)
                print(self.values)
        else:
            raise Exception("Stack does not exist")

    def pop(self, select_stack) -> Optional[int]:
        if self.is_empty(select_stack):
            raise Exception("Stack already empty")
        else:
            index_to_remove = self.index_of_top(select_stack)
            pop_value  = self.values[index_to_remove] 
            self.values[index_to_remove] = 0
            self._decrease_stack_size(select_stack)
            print(self.values)
            return pop_value
            

    def peek(self,select_stack):
        if self.is_empty:
            raise Exception("Stack is empty")
        else:
            return self.values[self.index_of_top(select_stack)]

    def _increase_stack_size(self, select_stack):
        self.current_sizes[select_stack - 1] += 1

    def _decrease_stack_size(self, select_stack):
        self.current_sizes[select_stack - 1] -= 1

    def index_of_top(self, select_stack):
        offset = (select_stack - 1) * self.stack_limit
        index = self.current_sizes[select_stack - 1] - 1
        return offset + index

    def is_full(self, select_stack):
        return self.current_sizes[select_stack - 1] == self.stack_limit

    def is_empty(self, select_stack):
        return self.current_sizes[select_stack - 1] == 0


if __name__ == "__main__":
    triple_stack = TripleStack(2)
    triple_stack.push(1, 10)
    print("before pop")
    triple_stack.push(1, 11)
    print("this is the peek value",triple_stack.peek(1))
    print("after pop")
    triple_stack.push(2, 10)
    triple_stack.push(2, 11)
    triple_stack.pop(2)
    triple_stack.pop(1)
    triple_stack.pop(1)

    triple_stack.push(3, 10)
    triple_stack.push(3, 11)

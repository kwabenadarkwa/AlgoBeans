# INFO: a heap is a complete tree where the parent node is always larger than the child nodes
# or the parent nodes are always smaller than the child nodes. difference between a min and a max heap
# this is my take at implementing a heap in python
# because of how a heap is in general we con't need to use an object to keep track of things
# we can basically use an array and then do some fancy math to be able to find where in the array to place things



#a max heap is the same just the opposite of what's happening here basically
class MinHeap:
    def __init__(self):
        self.size = 0
        self.items = []

    @staticmethod
    def get_left_child_index(index: int) -> int:
        return (2 * index) + 1

    @staticmethod
    def get_right_child_index(index: int) -> int:
        return (2 * index) + 2

    @staticmethod
    def get_parent_index(index: int) -> int:
        # floored for integer division so that it works for the right node case
        return (index - 1) // 2

    def has_left_child(self, index: int) -> bool:
        return MinHeap.get_left_child_index(index) < self.size

    def has_right_child(self, index: int) -> bool:
        return MinHeap.get_right_child_index(index) < self.size

    def has_parent(self, index: int) -> bool:
        return MinHeap.get_parent_index(index) >= 0

    def left_child(self, index: int) -> int:
        return self.items[MinHeap.get_left_child_index(index)]

    def right_child(self, index: int) -> int:
        return self.items[MinHeap.get_right_child_index(index)]

    def parent(self, index: int) -> int:
        return self.items[MinHeap.get_parent_index(index)]

    def swap(self, index_one: int, index_two: int) -> None:
        temp = self.items[index_two]
        self.items[index_two] = self.items[index_one]
        self.items[index_one] = temp

    def peek(self):
        if self.size == 0:
            raise Exception
        else:
            self.items[0]

    def poll(self) -> int:
        if self.size == 0:
            raise Exception
        else:
            item = self.items[0]
            self.items[0] = self.items.pop()
            self.size -= 1
            self.heapify_down()
            return item

    def add(self, value):
        self.items.append(value)
        self.size += 1
        self.heapify_up()

    def heapify_down(self):
        index = 0
        while self.has_left_child(index):

            smaller_child_index = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(
                index
            ) < self.left_child(index):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
                index = smaller_child_index

    def heapify_up(self):
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) > self.items[index]:
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)

if __name__ == "__main__":
    min_heap = MinHeap()
    min_heap.add(5)
    min_heap.add(150)
    min_heap.add(0)
    min_heap.add(7)
    min_heap.add(-7)
    min_heap.add(7)
    print(min_heap.poll())

# INFO
# Partition: Write code to partition a linked list around a value x, such that all nodes less than x come
# before all nodes greater than or equal to x. If x is contained within the list, the values of x only need
# to be after the elements less than x (see below). The partition element x can appear anywhere in the
# "right partition"; it does not need to appear between the left and right partitions.
# EXAMPLE
# Input: 3->5->8->5->10->2-> 1 [partition = 5]
# Output: 3 -> 1 -> 2 -> 10 -> 5 -> 5 -> 8
from linkedList import  SinglyLinkedList


def partition(llist: SinglyLinkedList, partition: int) -> SinglyLinkedList:
    current_node = llist.head
    right_partition = None
    left_partition = None

    while current_node:
        if current_node.value < partition:
            if left_partition is None:
                #INFO: I didn't need a singly linked list in this scenario I could have just used the regular ListNode to 
                # fix this problem 
                left_partition = SinglyLinkedList(current_node.value)
            else:
                left_partition.insert_at_tail(current_node.value)
        else:
            if right_partition is None:
                right_partition = SinglyLinkedList(current_node.value)
            else:
                right_partition.insert_at_tail(current_node.value)

        current_node = current_node.next

    if right_partition is not None and left_partition is not None:
        current_right_node = right_partition.head
        while current_right_node:
            left_partition.insert_at_tail(current_right_node.value)
            current_right_node = current_right_node.next

    return left_partition if left_partition is not None else llist




if __name__ == "__main__":
    llist = SinglyLinkedList(3)
    llist.insert_at_tail(5)
    llist.insert_at_tail(8)
    llist.insert_at_tail(5)
    llist.insert_at_tail(10)
    llist.insert_at_tail(2)
    llist.insert_at_tail(1)
    partition(llist,5).print()



# INFO:
# Question: Kth to Last
# Question Description:Implement an algorithm to find the kth to last element of a singly linked list
# Example:
# 1->2->3->4

from linkedList import SinglyLinkedList


def kth_to_last(llist: SinglyLinkedList, k: int):

    total_count = 0
    current_value = llist.head
    while current_value:
        total_count += 1
        current_value = current_value.next

    stop_count = total_count - k

    count = 0
    current_value = llist.head
    while current_value:
        count += 1
        if count == stop_count:
            return current_value.value
        current_value = current_value.next

def kth_to_last_rec(llist:SinglyLinkedList,k:int):
    if llist.head == None: 
        return 0

    index = kth_to_last_rec(llist.next,k) + 1
    if(index == k):
        print("the kth value is",llist.head.value)

    return index



if __name__ == "__main__":
    llist = SinglyLinkedList(1)
    llist.insert_at_tail(2)
    llist.insert_at_tail(3)
    llist.insert_at_tail(4)
    llist.insert_at_tail(5)

    llist.print()
    print(kth_to_last(llist,2))
    kth_to_last_rec(llist,2)

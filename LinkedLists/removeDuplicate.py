#INFO: 
#Question: Remove Dups
#Question Description: Write code to remove duplicates from an unsorted linked list.
#how would you solve this problem if a temporary buffer is not allowed?
#Example: 
# 1->2->1->1->4->None
#After removing dups

from linkedList import SinglyLinkedList

def remove_dups(llist:SinglyLinkedList):
    curr_pointer = llist.head
    while curr_pointer:
        prev_pointer = curr_pointer
        duplicate_searcher = curr_pointer.next
        while duplicate_searcher:
            if curr_pointer.value == duplicate_searcher.value:
                prev_pointer.next = duplicate_searcher.next
            else:
                prev_pointer = prev_pointer.next
            duplicate_searcher = duplicate_searcher.next
        curr_pointer = curr_pointer.next




if __name__ == "__main__":
    llist = SinglyLinkedList(1)
    llist.insert_at_tail(2)
    llist.insert_at_tail(10)
    llist.insert_at_tail(10)
    llist.insert_at_tail(1)


    llist.print()
    print("before")
    remove_dups(llist)
    print("after")
    llist.print()



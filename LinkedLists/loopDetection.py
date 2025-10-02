#INFO:
#Loop Detection: Given a circular linked list, implement an algorithm that returns the node at the
#beginning of the loop.
#DEFINITION
#Circular linked list: A (corrupt) linked list in which a node's next pointer points to an earlier node, so
#as to make a loop in the linked list.
#EXAMPLE
#Input: A -> B -> C -> D -> E -> C [the same C as earlier]
#Output: C

from typing import Optional
from linkedList import ListNode


#INFO:this is kind of different from the leetcode version. this one kind of says that the 
# thing you're dealing with is for sure a circular linkedlist so you don't have to even do the checks
def get_node_at_beginning_of_cycle(head:Optional[ListNode]):
    slow_pointer = head
    fast_pointer = head

    #my assumption 
    while True:
       slow_pointer = slow_pointer.next
       fast_pointer = fast_pointer.next.next
       if slow_pointer == fast_pointer:
            print("this is the value over there",slow_pointer.value)
            return slow_pointer
  
    #since they're moving in two's and 1's they're always going to meet first at the 
def get_node_at_beginning_of_cycle_better(head:Optional[ListNode]):
    slow_pointer = head
    fast_pointer = head


    while fast_pointer and fast_pointer.next:
       slow_pointer = slow_pointer.next
       fast_pointer = fast_pointer.next.next
       if slow_pointer == fast_pointer:
            break

    if fast_pointer is None and fast_pointer.next is None:
        return None

    slow_pointer = head
 
    while fast_pointer is not slow_pointer:
       slow_pointer = slow_pointer.next
       fast_pointer = fast_pointer.next
       if slow_pointer == fast_pointer:
            return slow_pointer


if __name__ == "__main__":
    first_value = ListNode(1)
    second_value = ListNode(2)
    third_value = ListNode(3)
    fourth_value = ListNode(4)
    fifth_value = ListNode(5)
    first_value.next = second_value
    second_value.next = third_value
    third_value.next = fourth_value
    fourth_value.next = fifth_value
    fifth_value.next = third_value

    print(get_node_at_beginning_of_cycle_better(first_value).value)

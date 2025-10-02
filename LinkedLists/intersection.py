# INFO:
# Intersection: Given two (singly) linked lists, determine if the two lists intersect. Return the
# intersecting node. Note that the intersection is defined based on reference, not value. That is, if the kth
# node of the first linked list is the exact same node (by reference) as the jth node of the second
# linked list, then they are intersecting.
from typing import Optional
from linkedList import ListNode

def get_intersection_node(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    set_of_list_nodes = set()

    curr_node = headA
    while curr_node:
        set_of_list_nodes.add(curr_node)
        curr_node = curr_node.next

    len_nodes = len(set_of_list_nodes) 
    prev_len = len(set_of_list_nodes) 

    curr_node = headB
    while curr_node:
        prev_len = len_nodes
        set_of_list_nodes.add(curr_node)
        len_nodes = len(set_of_list_nodes)
        if(len_nodes == prev_len):
            return curr_node
        curr_node = curr_node.next
    return None

def get_intersection_node_better(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    #we could return immediately if we checked the ends and they're not the same
    len_a = get_length(headA)
    len_b = get_length(headB)

    len_diff = abs(len_a - len_b)
    longer_list = headA if len_a >= len_b else headB
    shorter_list = headA if len_a < len_b else headB


    while len_diff > 0:
        longer_list = longer_list.next
        len_diff -= 1


    while longer_list and shorter_list:
        if longer_list == shorter_list:
            return longer_list
        longer_list = longer_list.next
        shorter_list = shorter_list.next

    return None


def get_length(head)->int:
    curr_node = head
    count = 0
    while curr_node:
        count += 1
        curr_node = curr_node.next
    return(count)


if __name__ == "__main__":
#INFO: this solution was tested on leetcode because I didn't want to struggle coming up with test cases to test with so yeah
 


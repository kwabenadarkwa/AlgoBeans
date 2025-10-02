#INFO:
# Implement a function to check if a linked list is a palindrome
from linkedList import ListNode


def check_palindrome(llist:ListNode)->bool:
    new_list = ListNode()
    new_list_head = new_list

    current_node = llist
    while current_node:
        new_list.value = current_node.value
        new_list.next = ListNode()
        new_list  = new_list.next
        current_node = current_node.next

    reversed_list = reverse_linked_list(llist)


    regular_list_current_node = new_list_head
    reversed_list_current_node = reversed_list

    while regular_list_current_node and reversed_list_current_node:
        if reversed_list_current_node.value != regular_list_current_node.value:
            return False
        regular_list_current_node = regular_list_current_node.next
        reversed_list_current_node = reversed_list_current_node.next

    return True

def reverse_linked_list(llist:ListNode)->ListNode:
    current_node = llist 
    next_node = None
    temp_next = None

    while current_node:
        next_node = current_node.next
        current_node.next = temp_next

        temp_next = current_node
        current_node = next_node

    return temp_next

if __name__ == "__main__":
    first_value = ListNode("a")
    second_value = ListNode("q")
    third_value = ListNode("q")
    fourth_value = ListNode("a")
    # third_value = ListNode(6)
    first_value.next = second_value
    second_value.next = third_value
    third_value.next = fourth_value
    print(check_palindrome(first_value))

 

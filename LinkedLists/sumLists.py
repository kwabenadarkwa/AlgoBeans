# INFO:
# Sum Lists: You have two numbers represented by a linked list, where each node contains a single
# digit. The digits are stored in reverse order, such that the 1's digit is at the head of the list. Write a
# function that adds the two numbers and returns the sum as a linked list.
# EXAMPLE
# Input: (7-> 1 -> 6) + (5 -> 9 -> 2).That is, 617 + 295.
# Output: 2 -> 1 -> 9.That is ,912.
# FOLLOW UP
# Suppose the digits are stored in forward order. Repeat the above problem.
# EXAMPLE
# Input: (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
# Output:9 -> 1 -> 2.Thatis,912.

from typing import Union

from linkedList import ListNode, SinglyLinkedList


# 1->1
# 2->5
# output 3->6
def sum_lists_backward_order(list_one: ListNode, list_two: ListNode):
    current_node_list_one = list_one
    current_node_list_two = list_two
    carry_over = 0
    sum_list = None
    head = None

    # assuming that the length of the lists are going to be the same and the sum
    # that it returns would also be the same length

    while current_node_list_one and current_node_list_two:
        temp_sum = (
            current_node_list_two.value + current_node_list_one.value + carry_over
        )

        if temp_sum > 9:
            carry_over = 1
            if sum_list is None:
                head = ListNode(temp_sum % 10)
                sum_list = head
            else:
                sum_list.next = ListNode(temp_sum % 10)
                sum_list = sum_list.next
        else:
            carry_over = 0
            if sum_list is None:
                head = ListNode(temp_sum)
                sum_list = head
            else:
                sum_list.next = ListNode(temp_sum)
                sum_list = sum_list.next

        current_node_list_one = current_node_list_one.next
        current_node_list_two = current_node_list_two.next

    assert sum_list is not None, "sum list should always return a value"
    return head


def sum_lists_backward_order_recursive(list_one: ListNode, list_two: ListNode):
    carry = 0
    return sum_lists(list_one, list_two, carry)


def sum_lists(
    list_one: Union[ListNode, None], list_two: Union[ListNode, None], carry: int
) -> Union[ListNode, None]:
    if list_one is None and list_two is None and carry == 0:
        return None

    node = ListNode()
    value = carry
    if list_one is not None:
        value += list_one.value
    if list_two is not None:
        value += list_two.value

    node.value = value % 10

    if list_one is not None or list_two is not None:
        next_value = sum_lists(
            list_one.next if list_one else None,
            list_two.next if list_two else None,
            1 if value > 9 else 0,
        )
        node.next = next_value

    return node


# this kind of assumes that the linked lists have the same length
# and wouldn't work for cases where the sum exceeds the length of the two linked lists
# (6 -> 1 -> 7) + (2 -> 9 -> 5).That is, 617 + 295.
# Output:9 -> 1 -> 2.Thatis,912.


def sum_lists_forward_order(list_one: ListNode, list_two: ListNode):
    carry_over = 0
    summation(list_one, list_two, carry_over)


def summation(list_one, list_two, carry_over: int):
    if list_one == None and list_two == None:
        return 0

    sum_for_level = (
        list_one.value
        + list_two.value
        + summation(list_one.next, list_two.next, carry_over)
    )

    if sum_for_level > 9:
        list_one.value = sum_for_level % 10
    else:
        list_one.value = sum_for_level

    return 1 if sum_for_level > 9 else 0


if __name__ == "__main__":
    first_value = ListNode(1)
    second_value = ListNode(2)
    # third_value = ListNode(6)
    first_value.next = second_value
    # second_value.next = third_value

    first_value_two = ListNode(1)
    second_value_two = ListNode(2)
    # third_value_two = ListNode(2)
    first_value_two.next = second_value_two
    # second_value_two.next = third_value_two

    print("before")
    print("first value", first_value.value)
    print("second value", second_value.value)
    # print("third value", third_value.value)

    print("first value two", first_value_two.value)
    print("second value two", second_value_two.value)
    # print("third value two", third_value_two.value)

    return_list = sum_lists_backward_order_recursive(first_value, first_value_two)

    print("after")
    print(return_list.value)
    print(return_list.next.value)
    # print(return_list.next.next.value)
    # first_value = ListNode(6)
    # second_value = ListNode(1)
    # third_value = ListNode(7)
    # first_value.next = second_value
    # second_value.next = third_value
    #
    # first_value_two = ListNode(2)
    # second_value_two = ListNode(9)
    # third_value_two = ListNode(5)
    # first_value_two.next = second_value_two
    # second_value_two.next = third_value_two
    #
    # print("before")
    # print("first value", first_value.value)
    # print("second value", second_value.value)
    # print("third value", third_value.value)
    #
    # print("first value two", first_value_two.value)
    # print("second value two", second_value_two.value)
    # print("third value two", third_value_two.value)
    #
    # return_list = sum_lists_forward_order(first_value, first_value_two)
    #
    # print("after")
    # print(first_value.value)
    # print(first_value.next.value)
    # print(first_value.next.next.value)
    #

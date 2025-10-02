#INFO:
#Delete Middle Node: Implement an algorithm to delete a node in the middle (i.e., any node but
#the first and last node, not necessarily the exact middle) of a singly linked list, given only access to
#that node.
#EXAMPLE
#Input: the node c from the linked list a->b->c->d->e->f
#Result: nothing is returned, but the new linked list looks like a->b->d->e->f

from linkedList import SinglyLinkedList, ListNode

#1->2->3->4
def delete_middle_node(node:ListNode)->bool:
    if(node == None or node.next == None):
        return False
    node.value = node.next.value
    node.next = node.next.next
    return True


if __name__ == "__main__":
    llist = SinglyLinkedList(1)
    llist.insert_at_tail(2)
    llist.insert_at_tail(3)
    llist.insert_at_tail(4)
    llist.insert_at_tail(5)
    print("before")
    llist.print()
    delete_middle_node(llist.return_middle_element())
    print("after")
    llist.print()






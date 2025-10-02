class ListNode:
    def __init__(self, val=0, next=None):
        self.value = val
        self.next = next


class SinglyLinkedList:
    def __init__(self, value: int):
        self.head = ListNode(value)

    def is_empty(self):
        return self.head == None

    def insert_at_head(self, value):
        previous_head = self.head
        self.head = ListNode(value)
        self.head.next = previous_head

    def insert_at_tail(self, value):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = ListNode(value)

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next
        print(None)

    def return_middle_element(self) -> ListNode:
        middle_node = self.head
        middle_node = middle_node.next
        return middle_node

class SinglyLinkedListNew:
    def __init__(self):
        pass

    def is_empty(self):
        return self.head == None

    def insert_at_head(self, value):
        previous_head = self.head
        self.head = ListNode(value)
        self.head.next = previous_head

    def insert_at_tail(self, value):
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = ListNode(value)

    def print(self):
        current_node = self.head
        while current_node:
            print(current_node.value, end="->")
            current_node = current_node.next
        print(None)

    def return_middle_element(self) -> ListNode:
        middle_node = self.head
        middle_node = middle_node.next
        return middle_node



if __name__ == "__main__":
    llist = SinglyLinkedList(5)
    llist.insert_at_head(8)
    llist.insert_at_head(7)
    llist.insert_at_head(17)
    llist.print()

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def insert_at_end(self, val) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def insert_at_beginning(self, val) -> None:
        new_node = ListNode(val)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        self.head = new_node
        new_node.next = curr

    def traverse(self) -> None:
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next
        print("None")


ll = LinkedList()
ll.insert_at_end(34)
ll.insert_at_end(54)
ll.insert_at_end(67)
ll.insert_at_beginning(23)
ll.traverse()

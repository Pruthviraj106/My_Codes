# A program to construct a singly linked list and then delete at specific position node of that singly linked list

class SinglyLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None

def createLinkedList(arr):
    head = None
    for data in arr:
        head = insertNodeAtEnd(head, data)
    return head

def insertNodeAtEnd(head, data):
    new_node = SinglyLinkedListNode(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    return head

def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next

def deleteNodeAtPosition(head, position):
    if head is None:
        return None
    if position == 0:
        return head.next
    current = head
    for _ in range(position-2):
        if current.next is None:
            return head
        current = current.next
    if current.next is None:
        return head
    current.next = current.next.next
    return head
n= int(input())
arr = list(map(int, input().split()))
position = int(input().strip())

head = createLinkedList(arr)

printLinkedList(head)
print()
head = deleteNodeAtPosition(head, position)
printLinkedList(head)

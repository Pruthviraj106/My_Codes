#A Program to  Delete head node in Singly-linked list

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

def deleteHeadNode(head):
    if head is None:
        return None
    return head.next

n = int(input())
value = list(map(int, input().split()))

head = createLinkedList(value)


printLinkedList(head)

head = deleteHeadNode(head)
print()
printLinkedList(head)

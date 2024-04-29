# Doubly Linked-List Construction
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
        

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

        
def constructLinkedList(arr):
    head = None
    for data in arr:
        head = insertNodeAtEnd(head, data)
    return head

def insertNodeAtEnd(head, data):
    new_node = Node(data)
    if head is None:
        return new_node
    current = head
    while current.next is not None:
        current = current.next
    current.next = new_node
    new_node.prev = current

    return head


def printLeftToRightManner(head):
    curr = head 
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.next 
    print()

def printRightToLeftManner(tail):
    tail = head 
    while tail.next != None:
        tail = tail.next 
 
    curr = tail
    while curr != None:
        print(curr.data, end = " ")
        curr = curr.prev 
    print()
    
n=int(input())
x = list(map(int, input().split()))
head = None 
for ele in x:
    head = insertNodeAtEnd(head,ele)
printLeftToRightManner(head)
printRightToLeftManner(head)

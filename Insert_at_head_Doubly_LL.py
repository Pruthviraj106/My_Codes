# Insert at head in Doubly-linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


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
    
def addNodeAtTailOfLinkedList(head, val):
    newBlock = Node(val)
 
    if head == None:
        return newBlock
 
    tail = head 
    while tail.next != None:
        tail = tail.next 
    tail.next = newBlock 
    newBlock.prev = tail 
    return head
    
def addNodeAtHeadOfLinkedList(head, val):
    newBlock = Node(val)
    if head == None:
        return newBlock
   
    newBlock.next = head 
    head.prev = newBlock 
    return newBlock

n = int(input())
values = list(map(int, input().split()))
new_value = int(input())

head = None
for value in values:
    head = addNodeAtTailOfLinkedList(head, value)

    
printLeftToRightManner(head)
printRightToLeftManner(head)



head = addNodeAtHeadOfLinkedList(head, new_value)

printLeftToRightManner(head)



tail = head 
while tail.next != None:
    tail = tail.next 
printRightToLeftManner(tail)

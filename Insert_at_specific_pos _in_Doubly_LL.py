# Insert at specific position in Doubly-linked list
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

def insertAtSpecificPosition(head, val, position):
    newBlock = Node(val)
    if head == None:
        return newBlock
 
    index = 1 
    curr = head 
 
    while index != position - 1 and curr.next != None:
        index += 1 
        curr = curr.next 
    nextNode = curr.next 
 
 
    newBlock.next = nextNode 
    nextNode.prev = newBlock 
    if nextNode != None:
        nextNode.prev = newBlock


 
    curr.next = newBlock 
    newBlock.prev = curr 
 
   
 
    return head

n = int(input())
values = list(map(int, input().split()))
pos, new_value = map(int, input().split())


head = None
for value in values:
    head = addNodeAtTailOfLinkedList(head, value)

    
printLeftToRightManner(head)
printRightToLeftManner(head)



head = insertAtSpecificPosition(head,new_value,pos)

printLeftToRightManner(head)



tail = head 
while tail.next != None:
    tail = tail.next 
printRightToLeftManner(tail)

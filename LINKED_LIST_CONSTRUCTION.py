#LINKED LIST CONSTRUCTION
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None
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
    return head
def printLinkedList(head):
    current = head
    while current is not None:
        print(current.data, end=" ")
        current = current.next

n = int(input().strip())
arr = list(map(int, input().split()))

head = constructLinkedList(arr)

printLinkedList(head)

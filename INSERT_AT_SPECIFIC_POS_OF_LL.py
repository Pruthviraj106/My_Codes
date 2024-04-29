# Function to Insert a node at a specific position in a linked list 
def insertNodeAtPosition(llist, data, position):
    # Write your code here
    new_node = SinglyLinkedListNode(data)
    
    if position == 0:
        new_node.next = llist
        return new_node

    current = llist
    for _ in range(position - 1):
        if current is None:
            break
        current = current.next

    if current is None:
        return llist
    new_node.next = current.next
    current.next = new_node

    return llist

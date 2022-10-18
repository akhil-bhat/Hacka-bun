# A Linked List Node
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
 
 
# Helper function to print a given linked list
def printList(msg, head):
 
    print(msg, end = '')
    ptr = head
    while ptr:
        print(ptr.data, end=' —> ')
        ptr = ptr.next
    print('None')
 
 
# Function to rearrange the given list such that every even node will be
# moved to the end of the list in reverse order.
def rearrange(head):
 
    # empty list
    if head is None:
        return
 
    # maintain two lists, odd and even
    odd = head
    even = prev = None
 
    # do for each odd node
    while odd and odd.next:
 
        # "move" next node (which will be even) to the front of the even list
        if odd.next:
            newNode = odd.next          # the front source node
            odd.next = odd.next.next    # advance the source
 
            newNode.next = even         # link the old dest off the new node
            even = newNode              # move dest to point to the new node
 
        # update `prev` and move to the next odd node
        prev = odd
        odd = odd.next
 
    # append even list to odd list
    if odd:
        odd.next = even
    else:
        prev.next = even
 
 
if __name__ == '__main__':
 
    # construct the first linked list
    head = None
    for i in reversed(range(7)):
        head = Node(i + 1, head)
 
    printList('Before: ', head)
 
    # rearrange the references to the given list
    rearrange(head)
    printList('After: ', head)

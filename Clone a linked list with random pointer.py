# A linked list node with a random pointer
class Node:
    # Constructor
    def __init__(self, data, next=None, random=None):
        self.data = data
        self.next = next
        self.random = random
 
 
# Recursive function to print a linked list
def traverse(head):
 
    if head is None:
        print('null')
        return
 
    # print current node data and random pointer data
    print(head.data, end='')
    print(f'({head.random.data})' if head.random else '(X)', end=' —> ')
 
    # recur for the next node
    traverse(head.next)
 
 
# Recursive function to copy random pointers from the original linked list
# into the cloned linked list using the dictionary
def updateRandomPointers(head, d):
 
    # base case
    if d.get(head) is None:
        return
 
    # update the random pointer of the cloned node
    d.get(head).random = d.get(head.random)
 
    # recur for the next node
    updateRandomPointers(head.next, d)
 
 
# Recursive function to clone the data and next pointer for each node
# of the linked list into a given dictionary
def cloneLinkedList(head, d):
 
    # base case
    if head is None:
        return None
 
    # clone all fields of the head node except the random pointer
 
    # create a new node with the same data as the head node
    d[head] = Node(head.data)
 
    # clone the next node
    d.get(head).next = cloneLinkedList(head.next, d)
 
    # return cloned head node
    return d.get(head)
 
 
# Function to clone a linked list having random pointers
def cloneList(head):
 
    # create a dictionary to store mappings from a node to its clone
    d = {}
 
    # clone data and next pointer for each node of the original
    # linked list and put references into the dictionary
    cloneLinkedList(head, d)
 
    # update random pointers from the original linked list in the dictionary
    updateRandomPointers(head, d)
 
    # return the cloned head node
    return d[head]
 
 
if __name__ == '__main__':
 
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
 
    head.random = head.next.next.next
    head.next.next.random = head.next
 
    print('Original Linked List:')
    traverse(head)
 
    clone = cloneList(head)
 
    print('\nCloned Linked List:')
    traverse(clone)
 

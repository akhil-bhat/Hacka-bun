import heapq
from heapq import heappop, heappush
 
 
# A class to store a heap node
class Node:
    def __init__(self, value, list_num, index):
        # `value` stores the element
        self.value = value
 
        # `list_num` stores the list number of the element
        self.list_num = list_num
 
        # `index` stores column number of the list from which element was taken
        self.index = index
 
    # Override the `__lt__()` function to make `Node` class work with min-heap
    def __lt__(self, other):
        return self.value < other.value
 
 
# Function to merge `M` sorted lists each of size `N` and
# print them in ascending order
def printSorted(lists):
 
    # push the first element of each list into the min-heap
    # along with the list number and their index in the list
    pq = [Node(lists[i][0], i, 0) for i in range(len(lists))]
    heapq.heapify(pq)
 
    # run till min-heap is empty
    while pq:
 
        # extract the minimum node from the min-heap
        min = heappop(pq)
 
        # print the minimum element
        print(min.value, end=' ')
 
        # take the next element from the "same" list and
        # insert it into the min-heap
        if min.index + 1 < len(lists[min.list_num]):
            min.index = min.index + 1
            min.value = lists[min.list_num][min.index]
            heappush(pq, min)
 
 
if __name__ == '__main__':
 
    lists = [
        [10, 20, 30, 40],
        [15, 25, 35, 45],
        [27, 29, 37, 48],
        [32, 33, 39, 50],
        [16, 18, 22, 28]
    ]
 
    printSorted(lists

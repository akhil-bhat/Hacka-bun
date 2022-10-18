import heapq
 
# Function to find the k'th largest element in a list using min-heap
def find_kth_largest(ints, k):
 
    # base case
    if not ints or len(ints) < k:
        exit(-1)
 
    # build a min-heap from the first `k` elements in the list
    pq = ints[0:k]
    heapq.heapify(pq)
 
    # do for remaining list elements
    for i in range(k, len(ints)):
        # if the current element is more than the root of the heap
        if ints[i] > pq[0]:
            # replace root with the current element
            heapq.heapreplace(pq, ints[i])
 
    # return the root of min-heap
    return pq[0]
 
 
if __name__ == '__main__':
 
    ints = [7, 4, 6, 3, 9, 1]
    k = 2
 
    print('k\'th largest element in the list is', find_kth_largest(ints, k))

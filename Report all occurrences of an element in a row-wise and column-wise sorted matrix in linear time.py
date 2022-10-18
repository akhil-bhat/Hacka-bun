def findElement(mat, key):
 
    # base case
    if not mat or not len(mat):
        return
 
    # `M × N` matrix
    (M, N) = (len(mat), len(mat[0]))
 
    # start from `(0, N-1)`, i.e., top-rightmost cell of the matrix
    i = 0
    j = N - 1
 
    # run till matrix boundary is reached
    while i <= M - 1 and j >= 0:
 
        # if the current element is less than the key, increment row index
        if mat[i][j] < key:
            i = i + 1
 
        # if the current element is more than the key, decrement col index
        elif mat[i][j] > key:
            j = j - 1
 
        # if the current element is equal to the key
        else:
            print("Element", key, "is found at position", (i, j))
            i = i + 1
            j = j - 1
 
 
if __name__ == '__main__':
 
    mat = [
        [-4, -3, -1, 3, 5],
        [-3, -2, 2, 4, 6],
        [-1, 1, 3, 5, 8],
        [3, 4, 7, 8, 9]
    ]
 
    findElement(mat, 3)

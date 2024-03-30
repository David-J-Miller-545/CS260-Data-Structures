def make_heap(arr):
    size = len(arr) - 1
    for i in range(size//2 - 1, -1, -1):
        downheap(arr, size, i)

def downheap(A, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left <= n and A[left] > A[largest]:
        largest = left
    if right <= n and A[right] > A[largest]:
        largest = right
    if largest != i:
        t = A[i]
        A[i] = A[largest]
        A[largest] = t
        downheap(A, n, largest)
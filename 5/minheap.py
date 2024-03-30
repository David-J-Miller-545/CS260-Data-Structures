def minmake_heap(arr):
    size = len(arr) - 1
    for i in range(size//2 - 1, -1, -1):
        mindownheap(arr, size, i)

def mindownheap(A, n, i):
    smallest = i
    left = 2*i + 1
    right = 2*i + 2
    if left <= n and A[left] < A[smallest]:
        smallest = left
    if right <= n and A[right] < A[smallest]:
        smallest = right
    if smallest != i:
        t = A[i]
        A[i] = A[smallest]
        A[smallest] = t
        mindownheap(A, n, smallest)
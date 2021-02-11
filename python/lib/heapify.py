import math

def max_heapify(A):
    """
    This method is used to maintain max-heap property in the binary tree data structure
    :param A: Elements of the binary tree as a list
    :return: Array satisfying the max-heap property
    """
    left = lambda x: (x << 1) + 1
    right = lambda x: (x << 1) + 2
    parent = lambda x: math.floor(math.log2(x))

    def recurse(A, i):
        l, r = left(i), right(i)
        if l < len(A) and A[l] > A[i]:
            largest = l
        else: largest = i
        if r < len(A) and A[r] > A[largest]:
            largest = r
        if largest != i:
            A[i], A[largest] = A[largest], A[i]
            recurse(A, largest)
    for index in reversed(range(len(A))):
        recurse(A, index)
    return A

def min_heapify(A):
    """
    This method is used to maintain min-heap property in the binary tree data structure
    :param A: Elements of the binary tree as a list
    :return: Array satisfying the min-heap property
    """
    left = lambda x: (x << 1) + 1
    right = lambda x: (x << 1) + 2
    parent = lambda x: math.floor(math.log2(x))

    def recurse(A, i):
        l, r = left(i), right(i)
        if l < len(A) and A[l] < A[i]:
            smallest = l
        else: smallest = i
        if r < len(A) and A[r] < A[smallest]:
            smallest = r
        if smallest != i:
            A[i], A[smallest] = A[smallest], A[i]
            recurse(A, smallest)
    for index in reversed(range(len(A))):
        recurse(A, index)
    return A

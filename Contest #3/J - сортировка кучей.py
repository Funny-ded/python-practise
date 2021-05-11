def heapsort(A):
    heapify_max_heap(A)
    print_array(A)
    for i in reversed(range(1, len(A))):
        A[:i + 1] = extract_max(A[:i + 1])[:i + 1]
        print_array(A)


def extract_max(A):
    if not len(A):
        return None
    tmp = A[0]
    A[0] = A[-1]
    A[:len(A) - 1] = sift_down(A[:len(A) - 1], 0)[:]
    A[-1] = tmp
    return A


def sift_down(A, x):
    while 2 * x + 1 < len(A):
        j = x
        if A[2 * x + 1] > A[x]:
            j = 2 * x + 1
        if 2 * x + 2 < len(A) and A[2 * x + 2] > A[j]:
            j = 2 * x + 2
        if x == j:
            break
        A[x], A[j] = A[j], A[x]
        x = j
    return A


def heapify_max_heap(A):
    for i in range(len(A)):
        lift_up_max_heap(A, i)


def print_array(A):
    print(' '.join(map(str, A)))


def lift_up_max_heap(A, x):
    while x != 0 and A[x] > A[(x - 1) // 2]:
        A[x], A[(x - 1) // 2] = A[(x - 1) // 2], A[x]





def heapify_fast(A):
    for i in reversed(range(len(A) // 2)):
        sift_down(A, i)
    return A





def extract_min(A):
    if not len(A):
        return None
    tmp = A[0]
    A[0] = A[-1]
    A.pop()
    sift_down(A,tmp)
    return tmp


def lift_up(A, x):
    while x != 0 and A[x] < A[(x - 1) // 2]:
        A[x], A[(x - 1) // 2] = A[(x - 1) // 2], A[x]
        x = (x - 1) // 2











A = list(map(int, input().split()))
heapsort(A)

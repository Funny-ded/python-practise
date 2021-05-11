def bubble_sort(A):
    print_array(A)
    for i in range(1, len(A)):
        for j in range(len(A) - i):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
                print_array(A)


def print_array(A):
    print(' '.join('{}'.format(A[i]) for i in range(len(A))))


bubble_sort(list(map(int, input().split())))

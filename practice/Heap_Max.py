class HeapMax:
    def __init__(self):
        self.values = []
        self.size = 0

    def insert(self, x):
        self.values.append(x)
        self.size += 1
        self.lift_up(self.size - 1)

    def lift_up(self, i):
        while i != 0 and self.values[i] > self.values[(i - 1) // 2]:
            self.values[i], self.values[(i - 1) // 2] = self.values[(i - 1) // 2], self.values[i]
            i = (i - 1) // 2

    def extract_max(self):
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        self.sift_down(0)
        return tmp

    def sift_down(self, i):
        while 2 * i + 1 < self.size:
            j = i
            if self.values[2 * i + 1] > self.values[i]:
                j = 2 * i + 1
            if 2 * i + 2 < self.size and self.values[2 * i + 2] > self.values[j]:
                j = 2 * i + 2
            if i == j:
                break
            self.values[i], self.values[j] = self.values[j], self.values[i]
            i = j


def heapify_fast(arr):
    heap = HeapMax()
    heap.values = arr[:]
    heap.size = len(arr)
    for i in reversed(range(heap.size // 2)):
        heap.sift_down(i)
    return heap


def heapsort(A):
    A[:] = heapify_fast(A).values[:]
    print_array(A)
    for i in range(len(A) - 1):
        tmp = A[0]
        A[:len(A) - 1 - i] = extract_max_arr(A[:len(A) - i]).values[:]
        A[len(A) - 1 - i] = tmp
        print_array(A)


def extract_max_arr(A):
    heap = HeapMax()
    heap.values[:] = A[:]
    heap.size = len(A)
    heap.extract_max()
    return heap


def print_array(A):
    print(' '.join(map(str, A)))


# A = Heapmax()
# A.values = [5, 3, 2]
# A.size = 3
# A.insert(10)
# print(A.values)
# print(A.extract_max(), A.values)
A = [3, 2, 5, 0, -1]
heapsort(A)
print(A)


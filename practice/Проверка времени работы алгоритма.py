from time import time
import random as rand
from contest_7 import E_district_reform as e
import test_J



def time_calc(f):
    t1 = time()
    i = 0
    count = 0
    while time() - t1 < 0.1:
        for _ in range(10**i):
            f()
        count += 10**i
        i += 1
    t2 = time()
    return (t2 - t1) / count


def f(p, r):
    p[:] = r[:]


if __name__ == '__main__':
    # input_data = list(map(int, input().split()))
    n, m = 1000, 100000  # n - num of vertexes, m - num of edges, s - start vertex, f - final vertex
    # regions = [-1] * (len(input_data) - 2)
    regions_num = rand.randint(0, 999)
    regions = [rand.randint(0, 999) for _ in range(regions_num)]
    gr = e.Graph(n + 1)
    gr.add_start(regions)
    for i in range(m):
        ed = (rand.randint(0, 999), rand.randint(0, 999), rand.randint(1, 1000000000))  # edge
        gr.add_edge(ed)
    d = [float('inf')] * (n + 1)  # distances
    d[-1] = -1
    h = e.HeapMin([n] + [i for i in range(n)])  # heap
    r = [-1] * (n + 1)  # regions of cities

    # r = [rand.randint(0, 1000) for _ in range(1000)]
    # p = [0] * 1000

    algo_time = 0
    algo_time += float(time_calc(lambda: e.Dijkstra_algo(h, gr, d, r)))
    print(algo_time, regions_num)

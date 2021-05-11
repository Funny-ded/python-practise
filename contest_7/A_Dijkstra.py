class HeapMin:
    def __init__(self, values):
        self.values = [0] * len(values)
        self.values[:] = values[:]
        self.elements = [0] * len(self.values)
        for element_index, element in enumerate(self.values):
            self.elements[element] = element_index
        self.size = len(self.values)

    # def insert(self, x):
    #     self.values.append(x)
    #     self.size += 1
    #     self.sift_up(self.size - 1)

    def dist_sift_up(self, element_index, distances):
        parent_index = (element_index - 1) // 2
        while element_index != 0 and distances[self.values[element_index]] < distances[self.values[parent_index]]:
            self.elements[self.values[element_index]], self.elements[self.values[parent_index]] = parent_index, element_index
            self.values[element_index], self.values[parent_index] = self.values[parent_index], self.values[element_index]
            element_index = parent_index
            parent_index = (element_index - 1) // 2

    def extract_min(self, distances):
        if not self.size:
            return None
        tmp = self.values[0]
        self.values[0] = self.values[-1]
        self.values.pop()
        self.size -= 1
        if self.size:
            self.elements[self.values[0]] = 0
        self.dist_sift_down(0, distances)
        return tmp

    def dist_sift_down(self, element_index, distances):
        youngest_child = 2 * element_index + 1
        oldest_child = 2 * element_index + 2
        while youngest_child < self.size:
            current_element = element_index
            if distances[self.values[youngest_child]] < distances[self.values[element_index]]:
                current_element = youngest_child
            if oldest_child < self.size and distances[self.values[oldest_child]] < distances[self.values[current_element]]:
                current_element = oldest_child
            if element_index == current_element:
                break
            self.elements[self.values[element_index]], self.elements[self.values[current_element]] = current_element, element_index
            self.values[element_index], self.values[current_element] = self.values[current_element], self.values[element_index]
            element_index = current_element
            youngest_child = 2 * element_index + 1
            oldest_child = 2 * element_index + 2


class Graph:

    def __init__(self, num_vertexes):
        self.graph = [set() for _ in range(num_vertexes)]

    def add_edge(self, edge):
        self.graph[edge[0]].add((edge[1], edge[2]))
        self.graph[edge[1]].add((edge[0], edge[2]))


def Dijkstra_algo(heap, graph, distances, parents):
    while heap.values:
        current_element = heap.extract_min(distances)
        if distances[current_element] == float('inf'):
            break
        for vertex, weight in graph.graph[current_element]:
            if distances[vertex] > distances[current_element] + weight:
                distances[vertex] = distances[current_element] + weight
                parents[vertex] = current_element
                heap.dist_sift_up(heap.elements[vertex], distances)


if __name__ == '__main__':
    n, m, s, f = map(int, input().split())  # n - num of vertexes, m - num of edges, s - start vertex, f - final vertex
    gr = Graph(n)
    for i in range(m):
        ed = tuple(map(int, input().split()))  # edge
        gr.add_edge(ed)
    d = [float('inf') for _ in range(n)]  # distances
    d[s] = 0
    h = HeapMin([s] + [i for i in range(n) if i != s])  # heap
    p = [None for _ in range(n)]  # parents
    Dijkstra_algo(h, gr, d, p)
    curr = f
    path = [f]
    while p[curr] is not None:
        path.append(p[curr])
        curr = p[curr]
    print(' '.join(map(str, reversed(path))))

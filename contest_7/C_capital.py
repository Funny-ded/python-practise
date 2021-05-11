class HeapMin:
    def __init__(self, values):
        self.values = [0] * len(values)
        self.values[:] = values[:]
        self.elements = [0] * len(self.values)
        for element_index, element in enumerate(self.values):
            self.elements[element] = element_index
        self.size = len(self.values)

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

    def sum_distances(self, start_vertex):
        heap = HeapMin([start_vertex] + [j for j in range(len(self.graph)) if j != start_vertex])
        distances = [float('inf')] * len(self.graph)
        distances[start_vertex] = 0
        sum_distances = [float('inf')] * len(self.graph)
        sum_distances[start_vertex] = 0 if start_vertex == 0 else float('inf')
        parents = [None for _ in range(n)]
        Dijkstra_algo(heap, self, distances, parents, sum_distances)
        return sum_distances[-1]


def Dijkstra_algo(heap, graph, distances, parents, sum_distances):
    while heap.values:
        current_element = heap.extract_min(distances)
        if distances[current_element] == float('inf'):
            break
        for vertex, weight in graph.graph[current_element]:
            if distances[vertex] > distances[current_element] + weight:
                distances[vertex] = distances[current_element] + weight
                parents[vertex] = current_element
                heap.dist_sift_up(heap.elements[vertex], distances)
                while vertex < len(graph.graph) and distances[vertex] < float('inf'):
                    if vertex == 0:
                        sum_distances[vertex] = distances[vertex]
                    else:
                        sum_distances[vertex] = sum_distances[vertex - 1] + distances[vertex]
                    vertex = vertex + 1


if __name__ == '__main__':
    n, m = map(int, input().split())  # n - num of vertexes, m - num of edges
    gr = Graph(n)
    for i in range(m):
        ed = tuple(map(int, input().split()))  # edge
        gr.add_edge(ed)
    sums = [float('inf')] * n
    for s in range(n):
        sums[s] = gr.sum_distances(s)
    print(sums.index(min(sums)))

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
        self.graph = [dict() for _ in range(num_vertexes)]
        self.num_v = num_vertexes

    def add_edge(self, edge):
        vertex = edge[0]
        neigh_vertex = edge[1]
        weight = edge[2]
        self.graph[2 * vertex][2 * neigh_vertex + 1] = weight
        self.graph[2 * vertex + 1][2 * neigh_vertex] = weight
        self.graph[2 * neigh_vertex + 1][2 * vertex] = weight
        self.graph[2 * neigh_vertex][2 * vertex + 1] = weight

    def Dijkstra(self, start_vertex, end_vertex):
        start_vertex *= 2
        end_vertex *= 2
        distances = [float('inf')] * self.num_v
        distances[start_vertex] = 0
        parents = [None] * self.num_v
        heap = HeapMin([start_vertex] + [j for j in range(self.num_v) if j != start_vertex])
        while heap.size:
            vertex = heap.extract_min(distances)
            if distances[vertex] == float('inf'):
                break
            for neigh_vertex in self.graph[vertex]:
                weight = self.graph[vertex][neigh_vertex]
                if distances[neigh_vertex] > distances[vertex] + weight:
                    distances[neigh_vertex] = distances[vertex] + weight
                    parents[neigh_vertex] = vertex
                    heap.dist_sift_up(heap.elements[neigh_vertex], distances)
        return self.way(parents, end_vertex)

    @staticmethod
    def way(parents, end_vertex):
        if parents[end_vertex] is None:
            return [-1]
        way = []
        curr_vertex = end_vertex
        while curr_vertex is not None:
            way.append(curr_vertex // 2)
            curr_vertex = parents[curr_vertex]
        return reversed(way)


if __name__ == '__main__':
    n, m = map(int, input().split())
    gr = Graph(2 * n)
    for _ in range(m):
        gr.add_edge(tuple(map(int, input().split())))
    for _ in range(int(input())):
        print(*gr.Dijkstra(*list(map(int, input().split()))))

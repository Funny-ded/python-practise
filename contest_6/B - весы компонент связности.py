class Graph:
    def __init__(self):
        self.vertexes = 0
        self.offset = []
        self.edges = []
        self.weights = []

    def count_vertexes(self, count):
        self.vertexes = count
        self.offset = [0 for _ in range(self.vertexes + 1)]

    def create_edge(self, vertex_1, vertex_2, weight):
        self.edges.insert(self.offset[vertex_1], vertex_2)
        self.weights.insert(self.offset[vertex_1], weight)
        self.change_offset(vertex_1)
        self.edges.insert(self.offset[vertex_2], vertex_1)
        self.weights.insert(self.offset[vertex_2], weight)
        self.change_offset(vertex_2)

    def change_offset(self, vertex):
        for i in range(vertex + 1, self.vertexes + 1):
            self.offset[i] += 1

    def dfs(self, vertex=0, used=None):
        if used is None:
            used = set()
        if vertex in used:
            return used
        for v in self.edges[self.offset[vertex]:self.offset[vertex + 1]]:
            used.add(vertex)
            used = used.union(self.dfs(v, used))
        return used

    def is_connected(self):
        return True if len(self.dfs()) == len(self.offset) - 1 else False

    def components_weights(self):
        return [self.component_weight(c) for c in self.connected_components()]

    def component_weight(self, component):
        weight = 0
        for vertex1 in component:
            for vertex2 in component:
                if self.edge_between(vertex1, vertex2):
                    weight_index = self.edges[self.offset[vertex1]:self.offset[vertex1 + 1]].index(vertex2)
                    weight += self.weights[self.offset[vertex1]:self.offset[vertex1 + 1]][weight_index]
        return weight // 2

    def edge_between(self, vertex1, vertex2):
        if vertex2 not in self.edges[self.offset[vertex1]:self.offset[vertex1 + 1]]:
            return False
        return True

    def connected_components(self):
        components = []
        used = set()
        for i in range(self.vertexes):
            if i not in used:
                component = self.dfs(i)
                used = used.union(component)
                components.append(list(component))
        return components


if __name__ == '__main__':
    n, m = map(int, input().split())
    gr = Graph()
    gr.count_vertexes(n)
    for _ in range(m):
        v1, v2, w = map(int, input().split())
        gr.create_edge(v1, v2, w)
    w = sorted(gr.components_weights())
    for j in range(len(w)):
        print(w[j])

class Graph:

    def __init__(self, num_vertexes, edges):
        self.graph = [dict() for _ in range(num_vertexes)]
        self.add_edges(edges)
        self.num_v = num_vertexes

    def add_edges(self, edges):
        for vertex, neigh_vertex, weight in edges:
            self.graph[vertex][neigh_vertex] = weight
            self.graph[neigh_vertex][vertex] = weight

    def min_cost_tree(self):
        start_vertex = 0
        weight = 0
        tree = set()
        used = {start_vertex}
        edges = set()
        for neigh_vertex in self.graph[start_vertex]:
            edges.add((start_vertex, neigh_vertex))
        for _ in range(self.num_v - 1):
            min_edge = self.get_min_edge(edges)
            vertex, neigh_vertex = min_edge[0], min_edge[1]
            used.add(neigh_vertex)
            weight += self.graph[vertex][neigh_vertex]
            tree.add(min_edge)
            edges = self.update_edges(edges, used, neigh_vertex)
        return weight, tree

    def get_min_edge(self, edges):
        weight = float('inf')
        edge = (0, 0)
        for vertex, neigh_vertex in edges:
            current_weight = self.graph[vertex][neigh_vertex]
            if weight > current_weight:
                weight = current_weight
                edge = vertex, neigh_vertex
        return edge

    def update_edges(self, edges, used, vertex):
        edges_changed = set()
        for vertex1, vertex2 in edges:
            if vertex2 not in used:
                edges_changed.add((vertex1, vertex2))
        for neigh_vertex in self.graph[vertex]:
            if neigh_vertex not in used:
                edges_changed.add((vertex, neigh_vertex))
        return edges_changed


if __name__ == '__main__':
    n, m = map(int, input().split())
    e = []
    for i in range(m):
        e.append(tuple(map(int, input().split())))
    gr = Graph(n, e)
    w, tr = gr.min_cost_tree()
    print(w)
    for ed in tr:
        print(*ed)

class WayException(Exception):
    pass


class TransportNetwork:

    def __init__(self, num_vertexes, edges):
        self.graph = [[] for _ in range(num_vertexes)]
        self.source = 0
        self.stock = num_vertexes - 1
        self.create_network(edges)

    def create_network(self, edges):
        for edge in edges:
            self.graph[edge[0]].append(edge[1])

    def ways(self):
        count_ways = 0
        while True:
            way = []
            self.dfs_any_way(way)
            if not way:
                break
            count_ways += 1
            self.rebuild(way)
        return count_ways

    def dfs_any_way(self, way):
        used = [False] * len(self.graph)
        parents = [None] * len(self.graph)
        try:
            self.dfs_way(self.source, used, parents, way)
        except WayException:
            return

    def dfs_way(self, curr_vertex, used, parents, way):
        used[curr_vertex] = True
        for neigh_vertex in self.graph[curr_vertex]:
            if neigh_vertex == self.stock:
                used[neigh_vertex] = True
                parents[neigh_vertex] = curr_vertex
                self.create_way(parents, way)
                raise WayException
            if not used[neigh_vertex]:
                parents[neigh_vertex] = curr_vertex
                self.dfs_way(neigh_vertex, used, parents, way)

    def create_way(self, parents, way):
        curr_vertex = self.stock
        while parents[curr_vertex] is not None:
            way.append(curr_vertex)
            curr_vertex = parents[curr_vertex]
        way.append(self.source)
        way.reverse()

    def rebuild(self, way):
        for j in range(len(way) - 1):
            self.change_edge(way[j], way[j + 1])

    def change_edge(self, vertex1, vertex2):
        edge_index = self.graph[vertex1].index(vertex2)
        self.graph[vertex1].pop(edge_index)
        self.graph[vertex2].append(vertex1)


if __name__ == '__main__':
    n, m, k = map(int, input().split())  # n - num of vertexes, m - num of edges, k - count of ways
    e = []  # edges
    for i in range(m):
        e.append(list(map(int, input().split())))
    n = TransportNetwork(n, e)  # n - network
    result = n.ways()
    if k <= result:
        print('YES')
    else:
        print('NO')

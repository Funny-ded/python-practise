class Graph:

    def __init__(self, num_vertexes, edges=None):
        self.graph = edges
        if edges is None:
            self.graph = []
        self.vertexes = num_vertexes

    def add_edge(self, edge):
        self.graph.append(edge)

    def Ford_Bellman(self, distances):
        change = False
        for _ in range(self.vertexes):
            change = False
            for edge in self.graph:
                if distances[edge[0]] < float('inf'):
                    if distances[edge[1]] > distances[edge[0]] + edge[2]:
                        distances[edge[1]] = distances[edge[0]] + edge[2]
                        change = True
        if change:
            distances[:] = [float('-inf')] * len(distances)


if __name__ == '__main__':
    # n - num of vertexes, m - num of edges, s - start vertex
    n, m, s = map(int, input().split())
    gr = Graph(n)
    d = [float('inf')] * n  # d - distances
    d[s] = 0  # distance for start vertex already defined
    for i in range(m):
        e = tuple(map(int, input().split()))  # e - edge
        gr.add_edge(e)
    gr.Ford_Bellman(d)
    for i in range(len(d)):
        print(d[i] if d[i] != float('inf') and d[i] != float('-inf') else 'UDF', end=' ')

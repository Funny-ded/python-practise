class Graph:

    def __init__(self, edges, count_vertexes):
        self.graph = dict()
        for v in range(count_vertexes):
            self.graph[v] = set()
        self.create_graph(edges)

    def create_graph(self, edges):
        for edge in edges:
            self.graph[edge[0]].add(edge[1])

    def cycle(self, vertex=0, white=None, grey=None, black=None):
        if white is None:
            white = list(k for k in range(vertex, len(self.graph)))
        if grey is None:
            grey = list()
        if black is None:
            black = list()
        cycle = []

        if vertex in white:
            white.remove(vertex)
            grey.append(vertex)
        for v in self.graph[vertex]:
            if cycle:
                break
            if v in white:
                cycle = self.cycle(v, white, grey, black)
                continue
            if v in grey:
                cycle = self.create_cycle(grey, v)
                return cycle
        if vertex in grey:
            grey.remove(vertex)
            black.append(vertex)
        return cycle

    def dfs(self, vertex, used, ans):
        if vertex not in used:
            used[vertex] = True
        for v in self.graph[vertex]:
            if v not in used:
                self.dfs(v, used, ans)
        ans.append(vertex)

    def topological_sort(self):
        used = dict()
        ans = []
        for vertex in self.graph:
            if vertex not in used:
                self.dfs(vertex, used, ans)
        ans[:] = ans[::-1]
        return ans

    @staticmethod
    def create_cycle(grey, start_vertex):
        return grey[grey.index(start_vertex):]

    @staticmethod
    def is_cycle():
        c = []
        ver = 0
        while not c and ver < n:
            c = graph.cycle(ver)
            ver += 1
        if c:
            return True
        else:
            return False


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph_edges = []
    for _ in range(m):
        graph_edges.append(list(map(int, input().split())))
    graph = Graph(graph_edges, n)
    graph_edges = None
    if graph.is_cycle():
        print('NO')
    else:
        print(' '.join(map(str, graph.topological_sort())))

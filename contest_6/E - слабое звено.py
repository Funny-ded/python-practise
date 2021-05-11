class GraphException(Exception):
    pass


class Graph:

    def __init__(self, edges, oriented=False):
        self.graph = dict()
        self.fill_vertexes(self.graph, edges)
        self.create_graph(edges, oriented)

    def create_graph(self, edges, oriented):
        for edge in edges:
            self.graph[edge[0]].add(edge[1])
            if not oriented:
                self.graph[edge[1]].add(edge[0])

    def dfs(self, articulation=False):
        """ start dfs and return object depends on parameters """
        colours = dict()
        for vertex in self.graph:
            colours[vertex] = 0  # 0 == white, p_test == grey, 2 == black. Set of colours is like a used set
            """For articulation point"""
        if articulation:
            articulation_points = set()
            f_up = dict()
            t_in = dict()
            timer = {'now': 0}
            for vertex in self.graph:
                self.dfs_articulation(vertex, colours, f_up, t_in, timer, articulation_points)
                if not articulation_points:
                    raise GraphException
                return articulation_points

    def dfs_articulation(self, vertex, colours, f_up, t_in, timer, articulation_points, prev=None):
        colours[vertex] = 2
        f_up[vertex] = t_in[vertex] = timer['now']
        timer['now'] += 1
        children = 0
        for neigh_vertex in self.graph[vertex]:
            if neigh_vertex == prev:
                continue
            if colours[neigh_vertex] == 2:
                f_up[vertex] = min(f_up[vertex], t_in[neigh_vertex])
            else:
                self.dfs_articulation(neigh_vertex, colours, f_up, t_in, timer, articulation_points, prev=vertex)
                f_up[vertex] = min(f_up[vertex], f_up[neigh_vertex])
                if f_up[neigh_vertex] >= t_in[vertex] and prev is not None:
                    articulation_points.add(vertex)  # vertex is articulation point
                children += 1
        if prev is None and children > 1:
            articulation_points.add(vertex)  # root is articulation point

    def articulation_point(self):
        try:
            return self.dfs(articulation=True)
        except GraphException:
            print('-1')
            exit(code=0)

    @staticmethod
    def fill_vertexes(graph, edges):
        for edge in edges:
            for vertex in edge:
                graph[vertex] = set()


if __name__ == '__main__':
    n, m = map(int, input().split())
    graph_edges = []
    for i in range(m):
        graph_edges.append(list(map(int, input().split())))
    gr = Graph(graph_edges, oriented=False)
    try:
        print(' '.join(map(str, gr.articulation_point())))
    except TypeError:
        print(-1)

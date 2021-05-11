class Queue:

    def append(self, name):
        self.create_part(name)

    def create_part(self, name):
        if not self.head:
            self.head = self.tail = self.create_node(name)
        else:
            self.tail['next'] = {'name': name, 'next': None, 'prev': None}
            self.tail['next']['prev'] = self.tail
            self.tail = self.tail['next']

    def pop_left(self):
        if not self.head:
            return
        if self.head is self.tail:
            value = self.head['name']
            self.head = self.tail = dict()
            return value
        value = self.head['name']
        self.head = self.head['next']
        self.head['prev'] = None
        return value

    def __init__(self):
        self.head = dict()
        self.tail = dict()

    def __str__(self):
        to_print = []
        curr = self.head
        while curr is not self.tail:
            to_print.append(curr['name'])
            curr = curr['next']
        to_print.append(curr['name'])
        return ' '.join(map(str, to_print))

    @staticmethod
    def create_node(name):
        return {'name': name, 'next': None, 'prev': None}


class Graph:

    def __init__(self, edges, count_vertexes, oriented=False):
        self.graph = dict()
        for v in range(count_vertexes):
            self.graph[v] = set()
        self.create_graph(edges, oriented)

    def create_graph(self, edges, oriented):
        for edge in edges:
            self.graph[edge[0]].add(edge[1])
            if not oriented:
                self.graph[edge[1]].add(edge[0])

    def distances(self, start_vertex):
        distances = [0] * len(self.graph)
        queue = Queue()
        queue.append(start_vertex)
        while queue.head:
            cur_vertex = queue.pop_left()
            for v in self.graph[cur_vertex]:
                if v != start_vertex and not distances[v]:
                    distances[v] = distances[cur_vertex] + 1
                    queue.append(v)
        return distances

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

    def is_cycle(self):
        c = []
        ver = 0
        while not c and ver < n:
            c = self.cycle(ver)
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
    start = 0
    dists = graph.distances(start)
    for i in range(len(dists)):
        print(dists[i])

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

    def __init__(self, edges, oriented=False):
        self.graph = dict()
        for v in edges:
            self.graph[v[0]] = set()
            self.graph[v[1]] = set()
        self.create_graph(edges, oriented)

    def create_graph(self, edges, oriented):
        for edge in edges:
            self.graph[edge[0]].add(edge[1])
            if not oriented:
                self.graph[edge[1]].add(edge[0])

    def distances(self, start_vertex):
        distances = dict()
        for v in self.graph:
            distances[v] = float('inf')
        distances[start_vertex] = 0
        queue = Queue()
        queue.append(start_vertex)
        while queue.head:
            cur_vertex = queue.pop_left()
            for v in self.graph[cur_vertex]:
                if v != start_vertex and distances[v] == float('inf'):
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


def coordinates(x, y):
    return '({}, {})'.format(x, y)


def land_to_graph(land):
    graph_list = []
    for x in range(len(land)):
        for y in range(len(land[x])):
            if land[x][y] == 'X':
                continue
            vertex_1 = coordinates(x, y)
            if 0 <= x - 1 < len(land) and land[x - 1][y] != 'X':
                vertex_2 = coordinates(x - 1, y)
                graph_list.append([vertex_1, vertex_2])
            if 0 <= x + 1 < len(land) and land[x + 1][y] != 'X':
                vertex_2 = coordinates(x + 1, y)
                graph_list.append([vertex_1, vertex_2])
            if 0 <= y - 1 < len(land[x]) and land[x][y - 1] != 'X':
                vertex_2 = coordinates(x, y - 1)
                graph_list.append([vertex_1, vertex_2])
            if 0 <= y + 1 < len(land[x]) and land[x][y + 1] != 'X':
                vertex_2 = coordinates(x, y + 1)
                graph_list.append([vertex_1, vertex_2])
    return graph_list


if __name__ == '__main__':
    n, m = map(int, input().split())
    x_start, y_start = map(int, input().split())
    start = coordinates(x_start, y_start)
    x_finish, y_finish = map(int, input().split())
    finish = coordinates(x_finish, y_finish)
    lan = []
    for i in range(n):
        lan.append(input())
    graph_edges = land_to_graph(lan)
    gr = Graph(graph_edges)
    try:
        dists = gr.distances(start)
        print(dists[finish] if dists[finish] < float('inf') else 'INF')
    except KeyError:
        print('INF')  # finish or start cell is blocking

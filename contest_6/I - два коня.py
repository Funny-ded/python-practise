class Deque:

    def __init__(self):
        self.head = dict()
        self.tail = dict()
        self.length = 0

    def __len__(self):
        return self.length

    def __bool__(self):
        return bool(self.head)

    def push_left(self, value):
        new_node = Deque.create_node(value, self.head or None)
        self.head = new_node
        self.length += 1

    def push_right(self, value):
        if not self.head:
            self.head = self.create_node(value)
            self.tail = self.head
            self.length += 1
            return
        self.tail['next'] = self.create_node(value)
        self.tail = self.tail['next']
        self.length += 1

    def get_left(self):
        try:
            return self.head['value']
        except KeyError:
            print('Error: Deque is empty')
            exit(code=1)

    def get_right(self):
        try:
            return self.tail['value']
        except KeyError:
            print('Error: Deque is empty')
            exit(code=1)

    def pop_left(self):
        pop_value = self.get_left()
        self.head = self.head['next'] or dict()
        if not self.head:
            self.tail = dict()
        self.length -= 1
        return pop_value

    def pop_right(self):
        pop_value = self.get_right()
        self.tail = self.tail['prev'] or dict()
        if not self.tail:
            self.head = dict()
        self.length -= 1
        return pop_value

    @staticmethod
    def create_node(value=None, follow=None, prev=None):
        return {'value': value, 'next': follow, 'prev': prev}


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

    def bfs(self, distances=False, start_vertex=None):
        """Start bfs depends on parameters"""
        """For distances"""
        if distances:
            distance = dict()
            for vertex in self.graph:
                distance[vertex] = float('inf')
            for vertex in self.graph:
                distance[vertex] = 0
                self.bfs_distances(start_vertex or vertex, distance)
                return distance


    def bfs_distances(self, start_vertex, distances):
        bfs_queue = Deque()
        bfs_queue.push_left(start_vertex)
        while bfs_queue:
            vertex = bfs_queue.pop_left()
            for neigh_vertex in self.graph[vertex]:
                if neigh_vertex != start_vertex and distances[neigh_vertex] != float('inf'):
                    distances[neigh_vertex] = distances[vertex] + 1
                    bfs_queue.push_right(neigh_vertex)

    def distances(self, start_vertex=None):
        return self.bfs(distances=True, start_vertex=start_vertex)

    @staticmethod
    def fill_vertexes(graph, edges):
        for edge in edges:
            for vertex in edge:
                graph[vertex] = set()


def chess_to_graph(edges, chars='abcdefgh', nums='12345678'):
    for i in range(8):
        for j in range(8):
            vertex_1 = chars[i] + nums[j]
            if 0 <= i + 2 < 8 and 0 <= j + 1 < 8:
                vertex_2 = chars[i + 2] + nums[j + 1]
                edges.append((vertex_1, vertex_2))
            if 0 <= i - 2 < 8 and 0 <= j + 1 < 8:
                vertex_2 = chars[i - 2] + nums[j + 1]
                edges.append((vertex_1, vertex_2))
            if 0 <= i + 1 < 8 and 0 <= j + 2 < 8:
                vertex_2 = chars[i + 1] + nums[j + 2]
                edges.append((vertex_1, vertex_2))
            if 0 <= i - 1 < 8 and 0 <= j + 2 < 8:
                vertex_2 = chars[i - 1] + nums[j + 2]
                edges.append((vertex_1, vertex_2))


def figure_dist(graph, start_cell, finish_cell):
    path_len = float('inf')
    for start_vertex in graph.graph:
        distances = inf_dict(graph)
        distances[start_vertex] = 0
        dist_queue = Deque()
        dist_queue.push_left(start_vertex)
        while dist_queue:
            vertex = dist_queue.pop_left()
            for neigh_vertex in graph.graph[vertex]:
                if neigh_vertex != start_vertex and distances[neigh_vertex] == float('inf'):
                    distances[neigh_vertex] = distances[vertex] + 1
                    dist_queue.push_right(neigh_vertex)
            if distances[start_cell] != float('inf') and distances[finish_cell] != float('inf'):
                if distances[start_cell] == distances[finish_cell]:
                    path_len = min(path_len, distances[start_cell])
                break
    return path_len


def inf_dict(graph):
    ans = dict()
    for vertex in graph.graph:
        ans[vertex] = float('inf')
    return ans


if __name__ == '__main__':
    start, finish = map(str, input().split())
    graph_edges = []
    chess_to_graph(graph_edges)
    gr = Graph(graph_edges)
    path = figure_dist(gr, start, finish)
    print(path if path < float('inf') else -1)

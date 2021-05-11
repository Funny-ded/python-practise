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

    def bfs(self, distances=False, start_vertex=None, short_cycle=False):
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
        """For shortest cycle"""
        if short_cycle:
            short_path = []
            for start_vertex in self.graph:
                distance = dict()
                parents = dict()
                path = []
                for vertex in self.graph:
                    distance[vertex] = float('inf')
                    parents[vertex] = None
                distance[start_vertex] = 0
                self.bfs_short_cycle(start_vertex, distance, parents, path)
                if len(path) and (not len(short_path) or len(path) < len(short_path)):
                    short_path[:] = path[::-1]
            return short_path

    def bfs_short_cycle(self, start_vertex, distances, parents, path):
        bfs_queue = Deque()
        bfs_queue.push_right(start_vertex)
        while bfs_queue:
            vertex = bfs_queue.pop_left()
            for neigh_vertex in self.graph[vertex]:
                if distances[neigh_vertex] == float('inf'):
                    distances[neigh_vertex] = distances[vertex] + 1
                    parents[neigh_vertex] = vertex
                    bfs_queue.push_right(neigh_vertex)
                elif neigh_vertex == start_vertex:
                    curr_vertex = vertex
                    while curr_vertex is not None:
                        path.append(curr_vertex)
                        curr_vertex = parents[curr_vertex]
                    return

    def bfs_distances(self, start_vertex, distances):
        bfs_queue = Deque()
        bfs_queue.push_right(start_vertex)
        while bfs_queue:
            vertex = bfs_queue.pop_left()
            for neigh_vertex in self.graph[vertex]:
                if neigh_vertex != start_vertex and distances[neigh_vertex] != float('inf'):
                    distances[neigh_vertex] = distances[vertex] + 1
                    bfs_queue.push_right(neigh_vertex)

    def distances(self, start_vertex=None):
        return self.bfs(distances=True, start_vertex=start_vertex)

    def shortest_cycle(self):
        cycle = self.bfs(short_cycle=True)
        if not cycle:
            raise GraphException
        return cycle

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
    gr = Graph(graph_edges, oriented=True)
    try:
        print(' '.join(map(str, gr.shortest_cycle())))
    except GraphException:
        print('NO CYCLES')

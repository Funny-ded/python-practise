from deq import Deque


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

    def dfs(self, connectivity_components=False, cycle=False, topological_sort=False, articulation=False):
        """ start dfs and return object depends on parameters """
        colours = dict()
        for vertex in self.graph:
            colours[vertex] = 0
        # 0 == white, 1 == grey, 2 == black. Set of colours is like a used set
        """For connectivity components"""
        if connectivity_components:
            components = set()
            for vertex in self.graph:
                component = set()
                if colours[vertex] == 0:  # if colour of vertex is white...
                    self.dfs_component(vertex, colours, component)
                    components.add(component)
            return components
        """For cycles"""
        if cycle:
            cycle = []
            for vertex in self.graph:
                if colours[vertex] == 0:
                    self.dfs_cycle(vertex, colours, potential_cycle=cycle)
            return cycle
        """For topological sort"""
        if topological_sort:
            topological = []
            for vertex in self.graph:
                if colours[vertex] == 0:
                    self.dfs_topological(vertex, colours, topological=topological)
            return topological[::-1]
        """For articulation point"""
        if articulation:
            f_up = dict()
            t_in = dict()
            timer = {'now': 0}
            articulation_points = set()
            for vertex in self.graph:
                self.dfs_articulation(vertex, colours, f_up, t_in, timer, articulation_points)
            if not articulation_points:
                raise GraphException
            return articulation_points

    def bfs(self, distances=False, start_vertex=None):
        """Start bfs depends on parameters"""
        """For distances"""
        if distances:
            distance = []
            for vertex in self.graph:
                self.bfs_distances(start_vertex or vertex, distance)
                return distance

    def dfs_component(self, vertex, colours, component):
        colours[vertex] = 2
        for neigh_vertex in self.graph[vertex]:
            if colours[neigh_vertex] == 0:
                self.dfs_component(neigh_vertex, colours, component)
        component.add(vertex)

    def dfs_cycle(self, vertex, colours, potential_cycle, prev=None):
        colours[vertex] = 1
        potential_cycle.append(vertex)
        for neigh_vertex in self.graph[vertex]:
            if colours[neigh_vertex] == 0:
                self.dfs_cycle(neigh_vertex, colours, potential_cycle, vertex)
            if potential_cycle:
                break
            if prev != neigh_vertex and colours[neigh_vertex] == 1:
                potential_cycle[:] = potential_cycle[potential_cycle.index(neigh_vertex):]
                break
        colours[vertex] = 2
        potential_cycle.pop()

    def dfs_topological(self, vertex, colours, topological):
        colours[vertex] = 2
        for neigh_vertex in self.graph[vertex]:
            if colours[neigh_vertex] == 0:
                self.dfs_topological(neigh_vertex, colours, topological)
        topological.append(vertex)

    def dfs_articulation(self, vertex, colours, f_up, t_in, timer, articulation_points, prev=None):
        colours[vertex] = 2
        f_up[vertex] = t_in[vertex] = timer['now']
        timer['now'] += 1
        children = 0
        for neigh_vertex in self.graph[vertex]:
            if neigh_vertex == prev:
                continue
            if colours[neigh_vertex] == 2:
                f_up[vertex] = min(f_up[vertex], f_up[neigh_vertex])
                continue
            if colours[neigh_vertex] == 0:
                self.dfs_articulation(neigh_vertex, colours, f_up, t_in, timer + 1, articulation_points, prev=vertex)
                f_up[vertex] = min(f_up[vertex], f_up[neigh_vertex])
                if f_up[neigh_vertex] >= t_in[vertex] and prev is not None:
                    articulation_points.add(vertex)  # vertex is articulation point
                children += 1
        if prev is None and children > 1:
            articulation_points.add(vertex)  # root is articulation point
        if prev is None and not articulation_points:
            raise GraphException

    def bfs_distances(self, start_vertex, distances):
        bfs_queue = Deque()
        bfs_queue.push_left(start_vertex)
        while bfs_queue:
            vertex = bfs_queue.pop_left()
            for neigh_vertex in self.graph[vertex]:
                if neigh_vertex != start_vertex and distances[neigh_vertex] != float('inf'):
                    distances[neigh_vertex] = distances[vertex] + 1
                    bfs_queue.push_right(neigh_vertex)

    def articulation_point(self):
        try:
            return self.dfs(articulation=True)
        except GraphException:
            print('There is no articulation points')
            exit(code=0)

    def topological_sort(self):
        """return topological sorted array of vertexes or Exception if there is a cycle"""
        try:
            if self.is_cycled():
                raise GraphException
        except GraphException:
            print('Graph cannot be topologically sorted because graph is cycled')
            exit(code=0)
        else:
            return self.dfs(topological_sort=True)

    def connectivity_components(self):  # looking for connectivity components
        return self.dfs(connectivity_components=True)

    def cycle(self):
        return self.dfs(cycle=True)

    def is_cycled(self):
        return self.cycle() or False

    def is_connective(self):
        return True if len(self.connectivity_components()) == 1 else False

    def distances(self, start_vertex=None):
        return self.bfs(distances=True, start_vertex=start_vertex)

    def create_cycle(self, start_vertex, end_vertex, colours, cycle):
        curr_vertex = start_vertex
        while curr_vertex != end_vertex:
            for vertex in self.graph[curr_vertex]:
                if colours[vertex] == 1:
                    cycle.append(vertex)

    @staticmethod
    def fill_vertexes(graph, edges):
        for edge in edges:
            for vertex in edge:
                graph[vertex] = set()

class OwnQueue:

    def __init__(self):
        self.head = dict()
        self.tail = dict()
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if not self.head:  # check if queue is empty
            return 'empty queue'
        queue_to_array = list()
        current_node = self.head
        while current_node:
            value = current_node['value']
            queue_to_array.append(value)
            current_node = current_node['next']
        return ' <- '.join(map(str, queue_to_array))

    def enqueue(self, name=None, value=None):
        if not self.head:
            self.head = self.create_part(name, value)
            self.tail = self.head
            self.length += 1
            return
        self.tail['next'] = self.create_part(name, value)
        self.tail = self.tail['next']
        self.length += 1

    def get(self):
        try:
            return self.head['value']
        except KeyError:
            print('Error: queue is empty')
            exit(code=1)

    def dequeue(self):
        pop_value = self.get()
        self.head = self.head['next'] or dict()
        self.length -= 1
        return pop_value

    @staticmethod
    def create_part(name=None, value=None, follow=None):
        return {'name': name, 'value': value, 'next': follow}


class TransportNetwork:

    def __init__(self, num_vertexes, edges):
        self.graph = dict()
        for i in range(num_vertexes):
            self.graph[i] = dict()
        self.source = 0
        self.stock = num_vertexes - 1
        self.num_v = num_vertexes
        self.create_network(edges)

    def create_network(self, edges):
        for edge in edges:
            self.graph[edge[0]][edge[1]] = TransportNetwork.edge(capacity=edge[2])
            self.graph[edge[1]][-edge[0]] = TransportNetwork.edge()

    def bfs(self, distances):
        bfs_queue = OwnQueue()
        bfs_queue.enqueue(value=self.source)
        while bfs_queue.length:
            curr_vertex = bfs_queue.dequeue()
            for neigh_vertex in self.graph[curr_vertex]:
                edge = self.graph[curr_vertex][neigh_vertex]
                if distances[abs(neigh_vertex)] == float('inf') and edge['flow'] < edge['capacity']:
                    distances[abs(neigh_vertex)] = distances[curr_vertex] + 1
                    bfs_queue.enqueue(value=abs(neigh_vertex))
        return distances[self.stock]

    def dfs(self, vertex, distances, flow):
        if not flow or vertex == self.stock:
            return flow
        for neigh_vertex in self.graph[vertex]:
            if distances[abs(neigh_vertex)] != distances[vertex] + 1:
                continue
            edge = self.graph[vertex][neigh_vertex]
            pushed_flow = self.dfs(abs(neigh_vertex), distances, min(flow, edge['capacity'] - edge['flow']))
            if pushed_flow:
                self.graph[vertex][neigh_vertex]['flow'] += pushed_flow
                self.graph[abs(neigh_vertex)][-vertex]['flow'] -= pushed_flow
                return pushed_flow
        return 0

    def dinic(self):
        flow = 0
        while True:
            distances = [float('inf')] * self.num_v
            distances[self.source] = 0
            if self.bfs(distances) == float('inf'):
                break
            pushed_flow = self.dfs(self.source, distances, float('inf'))
            while pushed_flow:
                flow += pushed_flow
                pushed_flow = self.dfs(self.source, distances, float('inf'))
        return flow

    @staticmethod
    def edge(flow=0, capacity=0):
        return {'flow': flow, 'capacity': capacity}


if __name__ == '__main__':
    n, m = map(int, input().split())  # n - num of vertexes, m - num of edges
    e = []  # edges list
    for _ in range(m):
        e.append(tuple(map(int, input().split())))  # append an input edge
    net = TransportNetwork(n, e)  # net - transport network
    print(net.dinic())  # Dinic algo

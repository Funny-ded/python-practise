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

    def __bool__(self):
        return bool(self.length)

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


class Graph:

    def __init__(self, num_vertexes, edges):
        self.graph = [set() for _ in range(num_vertexes)]
        for edge in edges:
            self.graph[edge[0]].add(edge[1])
            self.graph[edge[1]].add(edge[0])
        self.num_v = num_vertexes

    def bfs(self):
        tree = []
        bfs_queue = OwnQueue()
        bfs_queue.enqueue(value=0)
        distances = [float('inf')] * self.num_v
        distances[0] = 0
        while bfs_queue:
            curr_vertex = bfs_queue.dequeue()
            for neigh_vertex in self.graph[curr_vertex]:
                if distances[neigh_vertex] == float('inf'):
                    distances[neigh_vertex] = distances[curr_vertex] + 1
                    tree.append((curr_vertex, neigh_vertex))
                    bfs_queue.enqueue(value=neigh_vertex)
        return tree


if __name__ == '__main__':
    n, m = map(int, input().split())  # n - num of vertexes, m - num of edges
    e = []
    for i in range(m):
        e.append(tuple(map(int, input().split())))
    gr = Graph(n, e)
    tree = gr.bfs()
    for j in range(len(tree)):
        print(*tree[j])

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

    def enqueue(self, value=None):
        if not self.head:
            self.head = self.create_part(value)
            self.tail = self.head
            self.length += 1
            return
        self.tail['next'] = self.create_part(value)
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
    def create_part(value=None, follow=None):
        return {'value': value, 'next': follow}


class GraphFromTable:

    def __init__(self, num_rows, num_columns):
        """Граф из таблицы"""
        num_vertexes = num_rows * num_columns
        self.graph = [set() for _ in range(num_vertexes)]
        self.bfs_start = []
        self.create_graph(num_rows, num_columns)

    def create_graph(self, num_rows, num_columns):
        """Создание графа из таблицы"""
        for row in range(num_rows):
            for column in range(num_columns):
                vertex_1 = column + num_columns * row
                self.graph[vertex_1] = set()  # в словаре set из вершин, в которые есть ребро
                if 0 <= row - 1 < num_rows:
                    vertex_2 = column + num_columns * (row - 1)
                    self.graph[vertex_1].add(vertex_2)
                if 0 <= row + 1 < num_rows:
                    vertex_2 = column + num_columns * (row + 1)
                    self.graph[vertex_1].add(vertex_2)
                if 0 <= column - 1 < num_columns:
                    vertex_2 = column - 1 + num_columns * row
                    self.graph[vertex_1].add(vertex_2)
                if 0 <= column + 1 < num_columns:
                    vertex_2 = column + 1 + num_columns * row
                    self.graph[vertex_1].add(vertex_2)

    def bfs_table(self, dist_table):
        bfs_queue = OwnQueue()
        for vertex in self.bfs_start:  # обход стартовых точек
            dist_table[vertex] = 0
            bfs_queue.enqueue(vertex)
        while len(bfs_queue):  # непосредственно поиск расстояний bfs`ом
            vertex = bfs_queue.dequeue()
            for neigh_vertex in self.graph[vertex]:
                if dist_table[neigh_vertex] == -1:
                    dist_table[neigh_vertex] = dist_table[vertex] + 1
                    bfs_queue.enqueue(neigh_vertex)


if __name__ == '__main__':
    n, m = map(int, input().split())
    gr = GraphFromTable(n, m)
    output_table = [-1 for _ in range(n * m)]
    for i in range(n):
        input_table = list(map(int, input().split()))
        for j in range(len(input_table)):
            if input_table[j] == 1:
                gr.bfs_start.append(j + i * m)
    if len(gr.graph) == 0:
        print(0)
    else:
        gr.bfs_table(output_table)
        for i in range(n):
            print(' '.join(map(str, output_table[i * m:(i + 1) * m])))

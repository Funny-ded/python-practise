class Graph:
    def __init__(self):
        self.vertexes = 0
        self.offset = []
        self.edges = []

    def count_vertexes(self, count):
        self.vertexes = count
        self.offset = [0 for _ in range(self.vertexes + 1)]

    def create_edge(self, vertex_1, vertex_2):
        self.edges.insert(self.offset[vertex_1], vertex_2)
        self.change_offset(vertex_1)
        self. edges.insert(self.offset[vertex_2], vertex_1)
        self.change_offset(vertex_2)

    def change_offset(self, vertex):
        for i in range(vertex + 1, self.vertexes + 1):
            self.offset[i] += 1

    def dfs(self, vertex=0, used=None):
        if used is None:
            used = set()
        if vertex in used:
            return used
        for v in self.edges[self.offset[vertex]:self.offset[vertex + 1]]:
            used.add(vertex)
            used.intersection(self.dfs(v, used))
        return used

    def is_connected(self):
        return True if len(self.dfs()) == len(self.offset) - 1 else False


if __name__ == '__main__':
    n = int(input())
    m = int(input())
    gr = Graph()
    gr.count_vertexes(n)
    for _ in range(m):
        v1, v2 = map(int, input().split())
        gr.create_edge(v1, v2)
    if gr.is_connected():
        print('YES')
    else:
        print('NO')

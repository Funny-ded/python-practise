class GraphException(Exception):
    pass


n = int(input())
graph = [[] for _ in range(n)]
try:
    for i in range(n):
        graph[i] = list(map(int, input().split()))
        if graph[i][i] != 0:
            raise GraphException('loop')
        for j in range(n):
            if graph[i][j] > 1 or graph[i][j] < 0:
                raise GraphException('not simple')
        for j in range(i + 1):
            if graph[i][j] != graph[j][i]:
                raise GraphException('oriented')
except GraphException:
    print('NO')
else:
    print('YES')

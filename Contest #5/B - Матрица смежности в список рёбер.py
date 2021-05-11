n = int(input())
weight = [0 for _ in range(n * n)]
edges = [x for _ in range(n) for x in range(n)]
offset = [x for x in range(0, n * n + 1, n)]
for i in range(n):
    i_str = list(map(int, input().split()))
    weight[offset[i]:offset[i + 1]] = i_str[:]
for i in range(n):
    for j in range(n):
        if weight[offset[i]:offset[i + 1]][j] == 0:
            continue
        else:
            print(i, edges[offset[i]:offset[i + 1]][j], weight[offset[i]:offset[i + 1]][j])

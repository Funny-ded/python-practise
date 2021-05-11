def change(a, x):
    for i in range(x + 1, len(a)):
        a[i] += 1


def is_right_offset(a):
    global n
    for i in range(len(a) - 1):
        if a[i + 1] - a[i] != n - 1:
            return False
    return True


n, m = map(int, input().split())
edges = []
offset = [0 for i in range(n + 1)]
for i in range(m):
    v1, v2 = map(int, input().split())
    if v1 in edges[offset[v2]:offset[v2 + 1]] or v2 in edges[offset[v1]:offset[v1 + 1]] or v1 == v2:
        continue
    else:
        edges.insert(offset[v1], v2)
        change(offset, v1)
        edges.insert(offset[v2], v1)
        change(offset, v2)
if is_right_offset(offset):
    print('YES')
else:
    print('NO')

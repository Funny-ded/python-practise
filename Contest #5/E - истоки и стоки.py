def remove_origins(a, s):
    global edge_symbol
    for i in range(len(s)):
        if s[i] == edge_symbol:
            a[i] = None


def origins_check(a):
    while None in a:
        a.remove(None)


edge_symbol = 1
n = int(input())
origins = [x for x in range(1, n + 1)]
drains = []
for i in range(n):
    i_str = list(map(int, input().split()))
    if edge_symbol in i_str:
        remove_origins(origins, i_str)
    else:
        drains.append(i + 1)
origins_check(origins)
print(' '.join(map(str, origins)))
print(' '.join(map(str, drains)))

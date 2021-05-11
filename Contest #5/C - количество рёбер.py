n = int(input())
edge_count = 0
for i in range(n):
    i_str = list(map(int, input().split()))
    for j in range(i + 1, n):
        if i_str[j] == 1:
            edge_count += 1
print(edge_count)

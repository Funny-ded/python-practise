class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0


def insb(ll, value):
    tmp = Node(value)
    if ll.size != 0:
        ll.tail.next = tmp
    else:
        ll.head = tmp
    ll.tail = tmp
    ll.size += 1


def rem_fr(ll):
    ll.head = ll.head.next
    ll.size -= 1
    if ll.size == 0:
        ll.tail = None


def bfs(ones, used, length, adj):
    q = LinkedList()
    for k in range(len(ones)):
        insb(q, ones[k])
        used[ones[k]] = True
        length[ones[k]] = 0
    while q.size != 0:
        w = q.head.value
        rem_fr(q)
        for v in adj[w]:
            if not used[v]:
                length[v] = length[w] + 1
                insb(q, v)
                used[v] = True


def table_to_adj(adj, n, m):
    for i in range(n):
        for j in range(m):
            if i == 0 and i != n-1:
                adj[j + i * m].add(j + (i+1)*m)
            elif i != 0 and i == n-1:
                adj[j + i * m].add(j + (i-1)*m)
            else:
                adj[j + i * m].add(j + (i+1) * m)
                adj[j + i * m].add(j + (i-1) * m)
            if j == 0 and j != m-1:
                adj[j + i * m].add(j + 1 + i*m)
            elif j != 0 and j == m-1:
                adj[j + i * m].add(j - 1 + i*m)
            else:
                adj[j + i * m].add(j + 1 + i * m)
                adj[j + i * m].add(j - 1 + i * m)


if __name__ == '__main__':
    n, m = map(int, input().split())
    field = []
    adj = [set() for _ in range(n*m)]
    used = [False]*n*m
    length = [-1]*n*m
    for _ in range(n):
        li = list(map(int, input().split()))
        field.append(li)
    if n == m == 1:
        print('0')
        exit()
    for i in range(n):
        for j in range(m):
            if i == 0 and i != n-1:
                adj[j + i * m].add(j + (i+1)*m)
            elif i != 0 and i == n-1:
                adj[j + i * m].add(j + (i-1)*m)
            else:
                adj[j + i * m].add(j + (i+1) * m)
                adj[j + i * m].add(j + (i-1) * m)
            if j == 0 and j != m-1:
                adj[j + i * m].add(j + 1 + i*m)
            elif j != 0 and j == m-1:
                adj[j + i * m].add(j - 1 + i*m)
            else:
                adj[j + i * m].add(j + 1 + i * m)
                adj[j + i * m].add(j - 1 + i * m)
    ones = []
    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                ones.append(i*m+j)
    bfs()
    for i in range(n):
        for j in range(m):
            print(length[i*m+j], end=' ')
        print()

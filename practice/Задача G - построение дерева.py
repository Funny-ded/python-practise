class Tree:
    def __init__(self, seq):
        self.seq = seq
        self.tree = self.create_node(start=0, count=len(seq))
        self.create_branch(self.tree)

    def create_branch(self, node):
        if node['count'] > 1:

            count = node['count'] - node['count'] // 2
            start = node['start'] + node['count'] // 2
            node['rc'] = self.create_node(start=start, count=count)
            self.create_branch(node['rc'])

            count = node['count'] // 2
            start = node['start']
            node['lc'] = self.create_node(start=start, count=count)
            self.create_branch(node['lc'])

            node['sum'] = node['lc']['sum'] + node['rc']['sum']
        else:
            node['sum'] = self.seq[node['start']]

    def create_node(self, start=None, count=None):
        return {'sum': 0, 'lc': None, 'rc': None, 'start': start, 'count': count}

    def sum(self, l, r):
        return self._sum(self.tree, l, r)

    def _sum(self, node, l, r):
        # нет пересечения
        if l >= node['start'] + node['count'] or r < node['start']:
            return 0
        # полное включение
        if l <=node['start'] and r >= node['start'] + node['count'] - 1:
            return node['sum']
        return self._sum(node['lc'], l, r) + self._sum(node['rc'], l, r)

    def process_request(self, request):
        return self.sum(*request)


num_count = int(input())
seq = [int(x) for x in input().split()]
tree = Tree(seq)
request_count = int(input())
result = []
for _ in range(request_count):
    request = list(map(int, input().split()))
    result.append(tree.process_request(request))
print(' '.join(map(str, result)))


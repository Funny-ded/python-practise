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

            node['max'] = max(node['lc']['max'], node['rc']['max'])
        else:
            node['max'] = self.seq[node['start']]

    def create_node(self, start=None, count=None):
        return {'max': None, 'lc': None, 'rc': None, 'start': start, 'count': count}

    def find_max(self, l, r):
        return self._find_max(self.tree, l, r)

    def _find_max(self, node, l, r):
        if l >= node['start'] + node['count'] or r < node['start']:
            return float('-inf')
        if l <= node['start'] and r >= node['start'] + node['count'] - 1:
            return node['max']
        return max(self._find_max(node['lc'], l, r), self._find_max(node['rc'], l, r))

    def update(self, number, index):
        self.seq[index] = number
        self._update(self.tree, number, index)

    def _update(self, node, number, index):
        if index >= node['start'] + node['count'] or index < node['start']:
            return
        if index >= node['start'] and index <= node['start'] + node['count'] - 1:
            if node['count'] == 1:
                node['max'] = number
            else:
                self._update(node['lc'], number, index)
                self._update(node['rc'], number, index)
                node['max'] = max(node['lc']['max'], node['rc']['max'])
    # def sum(self, l, r):
    #     return self._sum(self.tree, l, r)
    #
    # def _sum(self, node, l, r):
    #     # нет пересечения
    #     if l >= node['start'] + node['count'] or r < node['start']:
    #         return 0
    #     # полное включение
    #     if l <=node['start'] and r >= node['start'] + node['count'] - p_test:
    #         return node['sum']
    #     return self._sum(node['lc'], l, r) + self._sum(node['rc'], l, r)

    # def process_request(self, request):
    #     return self.sum(*request)


num_count = int(input())
seq = [int(x) for x in input().split()]
tree = Tree(seq)
request_count = int(input())
result = []
for i in range(request_count):
    request = list(map(str, input().split()))
    if request[0] == 'max':
        result.append(tree.find_max(int(request[1]), int(request[2])))
    elif request[0] == 'upd':
        tree.update(int(request[2]), int(request[1]))
print(' '.join(map(str, result)))


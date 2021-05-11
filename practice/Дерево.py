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
        if l <= node['start'] and r >= node['start'] + node['count'] - 1:
            return node['sum']
        return self._sum(node['lc'], l, r) + self._sum(node['rc'], l, r)

    def mean(self, l, r):
        return self.sum(l, r) / (r - l + 1)

    def upd(self, l, r, val):
        self._upd(self.tree, l, r, val)

    def _upd(self, node, l, r, val):
        # нет пересечения
        if l >= node['start'] + node['count'] or r < node['start']:
            return node['sum']
        # полное включение
        if l <= node['start'] and r >= node['start'] + node['count'] - 1 and node['count'] == 1:
            node['sum'] += val
            return node['sum']
        node['sum'] = self._upd(node['lc'], l, r, val) + self._upd(node['rc'], l, r, val)
        return node['sum']


if __name__ == '__main__':
    num_count = int(input())
    sequence = [int(x) for x in input().split()]
    tree = Tree(sequence)
    request_count = int(input())
    result = []
    for _ in range(request_count):
        request = input().split()
        if request[0] == 'mean':
            result.append("{:.3g}".format(tree.mean(int(request[1]), int(request[2]))))
        if request[0] == 'add':
            tree.upd(int(request[1]), int(request[2]), int(request[3]))
    print(' '.join(map(str, result)))

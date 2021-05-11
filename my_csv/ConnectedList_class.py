class ConnectedList:

    def create_part(self, name):
        if not self.head:
            self.head = self.tail = self.create_node(name)
        else:
            self.tail['next'] = {'name': name, 'next': None, 'prev': None}
            self.tail['next']['prev'] = self.tail
            self.tail = self.tail['next']

    def pop_left(self):
        if not self.head:
            return
        if self.head is self.tail:
            self.head = self.tail = dict()
            return
        self.head = self.head['next']
        self.head['prev'] = None

    def pop_right(self):
        if not self.tail:
            return
        if self.head is self.tail:
            self.head = self.tail = dict()
            return
        self.tail = self.tail['prev']
        self.tail['next'] = None

    def __init__(self):
        self.head = dict()
        self.tail = dict()

    def __str__(self):
        to_print = []
        curr = self.head
        while curr is not self.tail:
            to_print.append(curr['name'])
            curr = curr['next']
        to_print.append(curr['name'])
        return ' '.join(map(str, to_print))

    @staticmethod
    def create_node(name):
        return {'name': name, 'next': None, 'prev': None}


if __name__ == '__main__':
    c = ConnectedList()
    for i in range(int(input())):
        c.create_part(int(input()))
    print(c)
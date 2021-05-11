class Deque:

    def __init__(self):
        self.head = dict()
        self.tail = dict()
        self.length = 0

    def __len__(self):
        return self.length

    def __bool__(self):
        return bool(self.head)

    def push_left(self, value):
        new_node = Deque.create_node(value, self.head or None)
        self.head = new_node
        self.length += 1

    def push_right(self, value):
        if not self.head:
            self.head = self.create_node(value)
            self.tail = self.head
            self.length += 1
            return
        self.tail['next'] = self.create_node(value)
        self.tail = self.tail['next']
        self.length += 1

    def get_left(self):
        try:
            return self.head['value']
        except KeyError:
            print('Error: Deque is empty')
            exit(code=1)

    def get_right(self):
        try:
            return self.tail['value']
        except KeyError:
            print('Error: Deque is empty')
            exit(code=1)

    def pop_left(self):
        pop_value = self.get_left()
        self.head = self.head['next'] or dict()
        if not self.head:
            self.tail = dict()
        self.length -= 1
        return pop_value

    def pop_right(self):
        pop_value = self.get_right()
        self.tail = self.tail['prev'] or dict()
        if not self.tail:
            self.head = dict()
        self.length -= 1
        return pop_value

    @staticmethod
    def create_node(value=None, follow=None, prev=None):
        return {'value': value, 'next': follow, 'prev': prev}

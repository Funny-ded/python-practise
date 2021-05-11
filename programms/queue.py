class OwnQueue:

    def __init__(self):
        self.head = dict()
        self.tail = dict()
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if not self.head:  # check if queue is empty
            return 'empty queue'
        queue_to_array = list()
        current_node = self.head
        while current_node:
            value = current_node['value']
            queue_to_array.append(value)
            current_node = current_node['next']
        return ' <- '.join(map(str, queue_to_array))

    def enqueue(self, name=None, value=None):
        if not self.head:
            self.head = self.create_part(value)
            self.tail = self.head
            self.length += 1
            return
        self.tail['next'] = self.create_part(value)
        self.tail = self.tail['next']
        self.length += 1

    def get(self):
        try:
            return self.head['value']
        except KeyError:
            print('Error: queue is empty')
            exit(code=1)

    def dequeue(self):
        pop_value = self.get()
        self.head = self.head['next'] or dict()
        self.length -= 1
        return pop_value

    @staticmethod
    def create_part(name=None, value=None, follow=None):
        return {'name': name, 'value': value, 'next': follow}

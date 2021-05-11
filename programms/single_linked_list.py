class SLL:  # input format: [name, value] -> n times
    # push at the mid of the list is not realized. Must think about input
    def __init__(self):  # we save a head of the list and a tail of the list.
        self.head = dict()
        self.tail = dict()
        self.length = 0  # we also save a number of elements as a length of the list

    def __len__(self):
        return self.length

    def __str__(self):
        if not self.head:  # check if list is empty
            return 'empty list'
        sll_to_string = ''
        current_node = SLL.create_part(follow=self.head)
        while current_node is not self.tail:
            name = current_node['next']['name']
            value = current_node['next']['value']
            sll_to_string += 'name: {}, value: {} \n'.format(name, value)
            current_node = current_node['next']
        return sll_to_string

    def push(self, name=None, value=None):
        if not self.head:
            self.head = self.create_part(name, value)
            self.tail = self.head
            self.length += 1
            return
        self.tail['next'] = self.create_part(name, value)
        self.tail = self.tail['next']
        self.length += 1

    def get_left(self):
        try:
            return self.head['value']
        except KeyError:
            print('There is nothing in the list')

    def get_right(self):
        try:
            return self.tail['value']
        except KeyError:
            print('There is nothing in the list')

    def pop_left(self):
        if self.tail is self.head:
            pop_value = self.get_left()
            self.head = self.tail = dict()
            self.length -= 1
            return pop_value
        pop_value = self.get_left()
        self.head = self.head['next']
        self.length -= 1
        return pop_value

    def pop_name(self, name):
        if not self.head:
            print('List is empty')
            raise Exception
        if name == self.head['name']:
            return self.pop_left()
        pop_value = None
        current_node = self.head
        while current_node is not self.tail:
            if current_node['next']['name'] == name:
                pop_value = current_node['next']['value']
                current_node['next'] = current_node['next']['next']
                break
        return pop_value

    @staticmethod
    def create_part(name=None, value=None, follow=None):
        return {'name': name, 'value': value, 'next': follow}

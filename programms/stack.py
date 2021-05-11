class Stack:
    def __init__(self):
        self.head = dict()
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        if not self.head:  # check if stack is empty
            return 'empty stack'
        stack_to_array = list()
        current_node = self.head
        while current_node:
            value = current_node['value']
            stack_to_array.append(value)
            current_node = current_node['next']
        return ' -> '.join(map(str, stack_to_array))

    def push(self, value=None):
        new_node = Stack.create_node(value, self.head or None)
        self.head = new_node
        self.length += 1

    def get(self):  # or peek
        try:
            return self.head['value']
        except KeyError:
            print('Error: Stack is empty')
            exit(code=1)

    def pop(self):
        pop_value = self.get()
        self.head = self.head['next'] or dict()
        self.length -= 1
        return pop_value

    @staticmethod
    def create_node(value=None, follow=None):
        return {'value': value, 'next': follow}

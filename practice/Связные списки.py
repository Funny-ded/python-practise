tail = head = None


def push_left(obj):
    global tail
    global head
    if head is None:
        tail = head = obj
        return
    obj['next'] = head
    head = obj
    return


def push_right(obj):
    global tail
    global head
    if head is None:
        tail = head = obj
        return
    tail['next'] = obj
    tail = obj
    return


def pop_left():
    pass


def pop(i):
    global tail
    global head
    if i == 0:
        pop_left()
        return
    curr = head
    for j in range(i - 1):
        if curr is None:
            raise Exception('wrong index')
        curr = curr['next']
    if curr is None or curr['next'] is None:
        raise Exception('wrong index')
    result = curr['next']['v']
    if tail is curr['next']:
        tail = curr
        curr['next'] = None
    else:
        curr['next'] = curr['next']['next']
    return result

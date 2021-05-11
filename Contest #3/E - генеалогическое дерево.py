tree = {'C': {'A', 'B'}, 'F': {'C'}, 'D': {'C'}}


def parents(tree, name):
    set_ = set()
    for k in tree:
        if k == name:
            set_ = tree[k]
    return set_


def grandparents(tree, name):
    help_set = parents(tree, name)
    set_ = set()
    if help_set:
        for k in help_set:
            set_ |= parents(tree, k)
    return set_


def children(tree, name):
    set_ = set()
    for k in tree:
        if name in tree[k]:
            set_.add(k)
    return set_


def grandchildren(tree, name):
    help_set = children(tree, name)
    set_ = set()
    if help_set:
        for k in help_set:
            set_ |= children(tree, k)
    return set_


def siblings(tree, name):
    help_set = parents(tree, name)
    set_ = set()
    if help_set:
        for k in help_set:
            set_ |= children(tree, k)
    if name in set_:
        set_.remove(name)
    return set_


print(parents(tree, 'C'),
parents(tree, 'A'),
grandparents(tree, 'D'),
grandparents(tree, 'C'),
children(tree, 'A'),
children(tree, 'D'),
grandchildren(tree, 'A'),
grandchildren(tree, 'F'),
siblings(tree, 'F'),
siblings(tree, 'C'))


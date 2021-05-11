def remove(table, key):
    f = polynomial(key)
    x = search(table, key)
    if x == 'KeyError':
        return x
    return table[f % 10].pop(x)[2]


def search(table, key):
    f = polynomial(key)
    for i in range(len(table[f % 10])):
        if f == table[f % 10][i][0]:
            if key == table[f % 10][i][1]:
                return i
    return 'KeyError'


def polynomial(X, A=91, M=100):
    P = ord(X[0]) % M
    if len(X) == 1:
        return P
    for i in range(1, len(X)):
        P = (A * P + ord(X[i])) % M
    return P


example_table = [
    [], [],
    [
        [32, 'ONLY', 'pal;cw'],
        [62, 'INDUSTRY', 'lfow'],
        [72, 'LETRASET', 'awdwad'],
        [32, 'BEEN', 'lkawdk'],
    ],
    [], [], [], [], [], [], [],
]
print(remove(example_table, 'BEEN'))      # v1 == 'lkawdk'
print(remove(example_table, 'PRODUCT'))
print(example_table)# v2 == 'KeyError'
# таблица принимает вид (элемент с ключом 'BEEN' удалён)
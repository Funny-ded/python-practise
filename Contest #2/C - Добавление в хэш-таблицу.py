def insert_hash(hash, key, value, index):
    H = [hash, key, value]
    hash_table[index].append(H)


def polynomial(X, A=91, M=100):
    P = ord(X[0]) % M
    if len(X) == 1:
        return P
    for i in range(1, len(X)):
        P = (A * P + ord(X[i])) % M
    return P


def change_hash_value(index, info_num, new_value):
    hash_table[index][info_num][2] = new_value


size = 10
hash_table = list([] for _ in range(size))
N = int(input())
for i in range(N):
    x = input().split()
    f = polynomial(x[0])
    if len(hash_table[f % size]) == 0:                        # Проверяем, что пусто:
        insert_hash(f, x[0], x[1], f % size)                  # если пусто, то инсерт
    else:
        flag = False
        for i in range(len(hash_table[f % size])):
            if hash_table[f % size][i][0] == f:
                if x[0] == hash_table[f % size][i][1]:    # если нет - то проверяем совпадение
                    change_hash_value(f % size, i, x[1])  # если совпало, то замена
                    flag = True
                    break
        if not flag:
            insert_hash(f, x[0], x[1], f % size)              # если не совпало, то инсерт
for i in range(size):
    if len(hash_table[i]) != 0:
        print(i)
    for j in range(len(hash_table[i])):
        print(' '.join(map(str, hash_table[i][j])))


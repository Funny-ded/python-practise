d = dict()
for i in range(int(input())):
    name = input()
    if name in d:
        d[name] += 1
    else:
        d[name] = 1
for k in sorted(d, key=lambda k_: d[k_], reverse=True):
    print(k, d[k])

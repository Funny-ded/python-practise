def distance(x1, y1, x2, y2):
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1 / 2)


x_1, y_1 = map(int, input().split())
x_2, y_2 = map(int, input().split())
n = int(input())
flag = True
for i in range(1, n + 1):
    x, y = map(int, input().split())
    R_dog = distance(x, y, x_2, y_2)
    R_gopher = distance(x, y, x_1, y_1)
    if R_dog / R_gopher < 2:
        continue
    else:
        print(i)
        flag = False
        break
if flag:
    print('-p_test')

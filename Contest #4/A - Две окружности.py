x_1, y_1, r_1 = map(int, input().split())
x_2, y_2, r_2 = map(int, input().split())
R = ((x_2 - x_1) ** 2 + (y_2 - y_1) ** 2) ** (1 / 2)
if R > r_1 + r_2:
    print('NO')
elif R <= r_1 + r_2:
    if R + min(r_1, r_2) < max(r_1, r_2):
        print('NO')
    else:
        print('YES')

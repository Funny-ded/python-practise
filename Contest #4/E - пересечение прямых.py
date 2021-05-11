def is_crossing(P_1, P_2):
    if P_1[0] == P_2[0] == 0 or (P_2[0] != 0 and P_1[0] / P_2[0] == P_1[1] / P_2[1]):
        return False
    return True


def crossing_lines(P_1, P_2):
    X = [0, 0]
    X_0 = (P_1[1] * P_2[2] - P_1[2] * P_2[1]) / (P_1[0] * P_2[1] - P_1[1] * P_2[0])
    Y_0 = (P_2[0] * X_0 + P_2[2]) / (- P_2[1])
    X[0], X[1] = round(X_0), round(Y_0)
    return X


p1 = list(map(int, input().split()))
p2 = list(map(int, input().split()))
if is_crossing(p1, p2):
    print(' '.join(map(str, crossing_lines(p1, p2))))
else:
    print('NO')

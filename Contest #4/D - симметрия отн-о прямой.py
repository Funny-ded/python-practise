def vector_abs(r):
    return (r[0] ** 2 + r[1] ** 2) ** (1 / 2)


def scalar(r, a):
    return r[0] * a[0] + r[1] * a[1]


def symmetry(X, A, K, B):
    symmetry_point = [0, 0]
    X_0 = (X[0] * A[0] + X[1] * A[1] - B * A[1]) / (A[0] + K * A[1])
    Y_0 = K * X_0 + B
    symmetry_point[0], symmetry_point[1] = X_0, Y_0
    return new_point(symmetry_point, X)


def symmetry_(X, X_1, Y_1, X_2, Y_2):
    if X_1 - X_2 == 0:
        X_ = [2 * X_1 - X[0], X[1]]
        return X_
    if Y_1 - Y_2 == 0:
        X_ = [X[0], 2 * Y_1 - X[1]]
        return X_
    A = [X_1 - X_2, Y_1 - Y_2]
    K = (Y_1 - Y_2) / (X_1 - X_2)
    B = Y_1 - K * X_1
    return symmetry(X, A, K, B)


def new_point(A, R):
    R_ = [None, None]
    R_[0] = R[0] + 2 * (A[0] - R[0])
    R_[1] = R[1] + 2 * (A[1] - R[1])
    return R_


x1, y1, x2, y2 = map(int, input().split())
x = list(map(int, input().split()))
x_ = symmetry_(x, x1, y1, x2, y2)
for i in range(2):
    print(round(x_[i], 5), end=' ')

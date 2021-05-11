def new_point(A, R):
    R_ = [None, None]
    R_[0] = R[0] + 2 * (A[0] - R[0])
    R_[1] = R[1] + 2 * (A[1] - R[1])
    return R_


x_1, y_1, x_2, y_2, x_3, y_3 = map(int, input().split())
a, b, c = [x_1, y_1], [x_2, y_2], [x_3, y_3]
points = [a, b, c]
point_s = list(map(int, input().split()))
for i in range(3):
    r = new_point(point_s, points[i])
    print(' '.join(map(str, r)), end=' ')

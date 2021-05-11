def polynomial(A, M, X):
    P = ord(X[0]) % M
    if len(X) == 1:
        return P
    for i in range(1, len(x)):
        P = (A * P + ord(X[i])) % M
    return P


a, m = map(int, input().split())
x = input()
print(polynomial(a, m, x))

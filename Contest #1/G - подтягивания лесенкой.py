def sport(K, M, n=0, N=0):
    if not N:
        N = K
    return sport(K, M - 1, n + 1, N + 2 * K + 2 * n + 1) if M - 1 else N


print(sport(int(input()), int(input())))

def computer_game(A, n):
    if n <= 1:
        return 0
    F = [0] * len(A)
    F[1] = abs(A[1] - A[0])
    for i in range(2, len(A)):
        F[i] = min(abs(A[i] - A[i - 1]) + F[i - 1], 3 * abs(A[i] - A[i - 2]) + F[i - 2])
    return F[-1]


N = int(input())
array = [int(input()) for _ in range(N)]
print(computer_game(array, N))

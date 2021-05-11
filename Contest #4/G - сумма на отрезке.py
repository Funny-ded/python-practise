def sum_array(A):
    S = [0 for _ in range(len(A))]
    S[0] = A[0]
    for i in range(1, len(A)):
        S[i] = S[i - 1] + A[i]
    return S


n = int(input())
numbers = list(map(int, input().split()))
sums = [0 for _ in range(n)]
sums[:] = sum_array(numbers)[:]
num_req = int(input())
requests_answers = [0 for _ in range(num_req)]
for i in range(num_req):
    l, r = map(int, input().split())
    requests_answers[i] = sums[r] - sums[l] + numbers[l]
print(' '.join(map(str, requests_answers)))

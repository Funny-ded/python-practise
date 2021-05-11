N, M = map(int, input().split())
input_1, input_2 = set(map(int, input().split())), set(map(int, input().split()))
data_ = input_1 | input_2
print(len(input_1), len(input_2), len(data_))

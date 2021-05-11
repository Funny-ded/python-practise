input_ = [set(map(int, input().split())) for i in range(3)]
result = sorted(list(input_[1] & input_[2] - input_[0]))
print(' '.join(map(str, result)))

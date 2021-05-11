def dot_product(N, vector1, vector2):
    result = 0
    for i in range(N):
        result += vector1[i] * vector2[i]
    return result


print(dot_product(3, [1, 2, 3], [1, 2, 3]))
print(dot_product(3, [1, 2, 3], [4, 5, 6]))

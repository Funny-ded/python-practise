def factorize(x):
    for i in range(2, int(x ** 1/2)):
        while not x % i:
            x //= i
            print(i)
        if x == 1:
            break


factorize(int(input()))

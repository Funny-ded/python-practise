x = int(input())
digits = []
while x:
    x, n = divmod(x, 10)
    digits.append(n)
s = ''
print(' + '.join('{}*10^{}'.format(digits[len(digits) - 1 - i], len(digits) - 1 - i) for i in range(len(digits))))

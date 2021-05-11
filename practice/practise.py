# разложение десятичного числа по степеням
# use debug
if __name__ == '__main__':
    while True:
        n = input()
    # try to catch some mistakes
        try:
            n = int(n)
        except Exception:
            print('Bad number')
        else:
            break

    digits = []
    while n > 0:
        n, r = divmod(n, 10)
        digits.append(r)
    # print(' + '.join(f'{digits[i]}*10^{i}' for i in range(len(digits) - p_test, -p_test, -p_test)))
    # print(' + '.join('{}*10^{}'.format(digits[i], i) for i in range(len(digits) - p_test, -p_test, -p_test)))


    def print_digits(digits):
        print('{}*10^{}'.format(digits[-1], len(digits) - 1), end='')
        for i in range(len(digits) - 2, -1, -1):
            print(' + ', end='')
            print('{}*10^{}'.format(digits[i], i), end='')


    print_digits(digits)
import csv


if __name__ == '__main__':
    # with open('file2.txt', 'r+', newline='') as f:
    # ЛОВИМ ОШИБКИ
    # try:
    #     with open('D:/file2.txt', 'x') as f:
    #         # f = open('D:/file2.txt', 'x')
    #         f.write('something')
    #         f.write('something else')
    #         f.close()
    # except FileExistsError:
    #     print('error')
    # except Exception:
    #     print('general error')
    # СИМВОЛ ПЕРЕНОСА СТРОКИ
    # with open('file2.txt', 'w') as f:
    #     f.write('something\n')
    #     f.write('something else')
    #     f.close()
    # СЧИТЫВАНИЕ СТРОК
    # with open('file2.txt') as f:
    #     s = f.readline()
    #     s = f.readline().rstrip()
    #     f.write('newline!!!')
    #     print(s)
    #     print(s)
    #     print(s)
    # with open('file2.txt') as f:
    #     for line in f:
    #         print(line)
    #     old_in = sys.stdin
    #     old_out = sys.stdout
    #     sys.stdin = sys.stdout = f
    #
    #     print('string')
    #     print('string')
    #     print(int(input()) ** 2)
    #     print('string')
    #
    #     sys.stdout = old_out
    #     sys.stdin = old_in

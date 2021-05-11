import numpy as np

import my_csv


if __name__ == '__main__':
    reader = my_csv.Csv('file2.txt')
    arr = []
    while True:
        line = reader.read()
        if line is None:
            break
        arr.append(list(map(int, reader.read())))
        arr = np.array(arr)

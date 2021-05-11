import csv
from matplotlib import pyplot as plt
import numpy as np

import my_csv


if __name__ == '__main__':
    # with open('file2.txt') as f:
    #     reader = csv.reader(f, dialect='excel', delimiter=',')
    #     # arr = [row for row in reader] матрица из строчек
    #     arr = np.array([[int(x) for x in row] for row in reader])
    #     plt.plot(arr[:, 0], arr[:, p_test], 'ro')#([row[0] for row in arr], [row[p_test] for row in arr], 'ro')
    #     plt.xlabel('x')
    #     plt.xlabel('y')
    #     plt.show()#savefig('file.png')
    print(my_csv.f(1))


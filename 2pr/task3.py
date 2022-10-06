import numpy as np
x = int(input('Введите количество строк: \n'))
y = int(input('Введите количество столбцов: \n'))
n = np.random.randint(1, 100, (x, y))

print('Сгенерированная матрица: \n', n)

print(np.concatenate(n))

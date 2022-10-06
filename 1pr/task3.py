import math

a = int(input('Введите первую сторону треугольника: '))
b = int(input('Введите вторую сторону треугольника: '))
c = int(input('Введите третью сторону треугольника: '))

if (a + b < c) or (a + c < b) or (b + c < a):
    print('Такого треугольника не существует')
else:
    p = (a + b + c)/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print(s)
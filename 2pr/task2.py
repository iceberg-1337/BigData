n = int(input('Введите количество чисел: '))
m = []
for i in range(n):
    j = 0
    while j < i+1:
        m.append(i+1)
        j += 1
    if len(m) > n:
        break
m = m[0:n]
for i in m:
    print(i, end=" ")
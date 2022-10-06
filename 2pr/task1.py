num = int(input('Введите число: '))
sqr_sum = 0
sqr_sum += num ** 2
sum = 0
while True:
    sum += num
    if sum == 0:
        print(sqr_sum)
        break
    else:
        num = int(input('Введите число: '))
        sqr_sum += num ** 2
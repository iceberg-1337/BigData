def calc():
    first_number = int(input('Введите первое число: '))
    second_number = int(input('Введите второе число: '))
    op = input('Выберите операцию ( +, -, /, //, abs – модуль, pow или ** – возведение в степень) : ')
    if op == '+':
        res = first_number + second_number
        return str(first_number) + ' + ' + str(second_number) + ' = ' + str(res)
    elif op == '-':
        res = first_number - second_number
        return str(first_number) + ' - ' + str(second_number) + ' = ' + str(res)
    elif op == '/':
        res = first_number / second_number
        return str(first_number) + ' / ' + str(second_number) + ' = ' + str(res)
    elif op == '//':
        res = first_number // second_number
        return str(first_number) + ' // ' + str(second_number) + ' = ' + str(res)
    elif op == 'abs':
        return 'модуль ' + str(first_number) + ' = ' + str(abs(first_number)) + '\n' + \
               'модуль ' + str(second_number) + ' = ' + str(abs(second_number))
    elif op == '**':
        res = first_number ** second_number
        return str(first_number) + ' в степени ' + str(second_number) + ' = ' + str(res)
    else:
        return 'Неправильная операция'


while True:
    print(calc())

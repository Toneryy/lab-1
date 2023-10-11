import math


def main():
    choice = input('Какую операцию вы хотите выполнить:\n'
                   'Для выбора введите + , - , * , / , sqrt , **, sin, cos, tan, ctg, log '
                   'или СТОП для остановки программы\nРазделитель: "."\n')
    choice = choice.replace('^', '**')
    choice = choice.replace('ctg', '1/tan')
    choice = choice.replace('tg', 'tan')
    choice = choice.replace(',', '.')
    choice = choice.replace('стоп', 'СТОП')
    if choice not in ['+', '-', '*', '/', 'sqrt', '**', 'sin', 'cos', 'tan', '1/tan', 'log', 'СТОП']:
        print('Неизвестный ввод')
        return main()
    if choice == 'СТОП':
        return 'Вы закончили работать с калькулятором'
    else:
        if choice == 'log':
            try:
                a, b = map(float, input('Введите число и основание логарифма: ').split())
                a = a.replace(',', '.')
                b = b.replace(',', '.')
                print(int(math.log(a, b)))
                return main()
            except ValueError:
                print('Вы ввели не 2 числа, программа будет запущена заново')
                return main()


        if choice not in ['sqrt', 'sin', 'cos', 'tg', '1/tan', 'log']:
            try:
                print(f'Формат ввода: a b\nФормат вывода: a {choice} b')
                a, b = map(float, input('Введите два числа: ').split())
                if choice == '*':
                    return round(a * b, 3)
                if choice == '+':
                    return round(a + b, 3)
                if choice == '-':
                    return round(a - b, 3)
                try:
                    if choice == '/':
                        return round(a / b, 3)
                except ZeroDivisionError:
                    print('На ноль делить нельзя')
                    return main()
                if choice == '**':
                    return a ** b
            except ValueError:
                print('Вы ввели не 2 числа, программа будет запущена заново')
                return main()
        else:
            try:
                if choice == 'sqrt':
                    a = float(input('Введите число из которого будем извлекать корень: '))
                    return round(math.sqrt(a), 3)
            except ValueError:
                print('Вы ввели больше 1 числа, либо отрицательное число, программа будет запущена заново')
                return main()

            try:
                if choice == 'sin':
                    a = float(input('Введите радианы для поиска синуса: '))
                    return math.sin(math.radians(a))
            except ValueError:
                print('Вы ввели больше 1 числа, либо операции для данного числа не существует,'
                      ' программа будет запущена заново')
                return main()

            try:
                if choice == 'cos':
                    a = float(input('Введите радианы для поиска косинуса: '))
                    return math.cos(math.radians(a))
            except ValueError:
                print('Вы ввели больше 1 числа, либо операции для данного числа не существует,'
                      ' программа будет запущена заново')
                return main()

            try:
                if choice == 'tan':
                    a = float(input('Введите радианы для поиска тангенса: '))
                    return math.tan(math.radians(a))
            except ValueError:
                print('Вы ввели больше 1 числа, либо операции для данного числа не существует,'
                      ' программа будет запущена заново')
                return main()

            try:
                if choice == '1/tan':
                    a = float(input('Введите радианы для поиска котангенса: '))
                    return 1/math.tan(math.radians(a))
            except ValueError:
                print('Вы ввели больше 1 числа, либо операции для данного числа не существует,'
                      ' программа будет запущена заново')
                return main()
        if '<built-in function' in choice:
            return 'В функции sin(), cos(), tg(), ctg(), sqrt() нужно передать один аргумент!'
        else:
            return main()


result = main()
print(result)

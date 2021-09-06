# Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль.
# Проверьте его работу на данных, вводимых пользователем. При вводе пользователем нуля
# в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.


class My_ZeroDivisionError(Exception):
    def __init__(self, txt):
        self.txt = txt


try:
    x = float(input('Введите число: '))
    y = float(input('Делитель: '))
    if y == 0:
        raise My_ZeroDivisionError(f'Исключение. На ноль делить нельзя')

except (ValueError, My_ZeroDivisionError) as error:
    print(error)

else:
    print(f'Результат: {round(x / y, 2)}')

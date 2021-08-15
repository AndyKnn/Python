# Реализовать функцию, принимающую два числа (позиционные аргументы) и
# выполняющую их деление. Числа запрашивать у пользователя, предусмотреть
# обработку ситуации деления на ноль.

def my_func(num1, num2):
    result = num1 / num2
    print(f"Результат деления {num1} на {num2} равен >>> {round(result, 2)}")


print(f"Для выхода из цикла нажмите Ctrl+D")

while True:
    try:
        number1 = float(input(f"Введите первое число >>> "))
        number2 = float(input(f"Введите второе число >>> "))
        my_func(number1, number2)

    except ZeroDivisionError:
        print("Ошибка: деление на ноль")
        break
    except ValueError:
        print("Неверное число")
    except EOFError:
        break
